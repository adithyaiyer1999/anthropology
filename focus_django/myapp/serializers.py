from rest_framework import serializers
from .models import Project, URLSummary
from .ml_func import function_need
from .email_test import send_email
from .ignore_list import url_to_ignore
from .nomic import createNomicMap
class URLSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = URLSummary
        fields = ['url', 'prompt']

import random
from datetime import datetime
import uuid
timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
class ProjectSerializer(serializers.ModelSerializer):
    urls_and_summaries = URLSummarySerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['username','urls_and_summaries']


    def create(self, validated_data):
        nomic_data = []
        visited_url_list = []
        urls_and_summaries_data = self.initial_data.get('urls_and_summaries', [])
        project = Project.objects.create(username = "popatlal")
        text_summary ={}
        counter = 0
        for index,url_and_summary_data in enumerate(urls_and_summaries_data):
            def contains_substring(string, substrings):
                for substring in substrings:
                    if substring in string:
                        return True
                return False

            if url_and_summary_data['url'] in visited_url_list:
                continue

            visited_url_list.append(url_and_summary_data['url'])

            if contains_substring(url_and_summary_data['url'], url_to_ignore):
                continue

            text_returned = function_need(url_and_summary_data['url'],url_and_summary_data['prompt'])
            if 'Irrelevant' in text_returned:
                continue

            unique_string = str(uuid.uuid4())

            nomic_data.append({'url' :url_and_summary_data['url'] , 'id_':unique_string,'prompt':url_and_summary_data['prompt'],'row_number':'hello','text': text_returned,'undefined':None})
            text_summary[f"Article {counter+1}"+"::"+url_and_summary_data['url']]=text_returned
            counter+=1
            url_summary = URLSummary.objects.create(**url_and_summary_data)
            project.urls_and_summaries.add(url_summary)

        import json

        def save_json(data, filename):
            with open(filename, 'w') as json_file:
                json.dump(data, json_file, indent=4)

        # save_json(nomic_data, 'nomic_data_4.json')

        # if len(nomic_data)>23:
        nomic_url = createNomicMap(nomic_data)
        send_email(text_summary,nomic_url)
        return project