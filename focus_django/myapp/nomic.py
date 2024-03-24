import nomic
from nomic import atlas
import json
import pandas as pd
from nomic import AtlasDataset
nomic.login("nk-gMu-JRTuzF2U7SJMFJzgydePumSzhzdVsEXus4Kams8")

# with open('nomic_data.json', 'r') as file:
#     # Load the JSON data into a Python object
#     data = json.load(file)["urls_and_summary"]
import random
# def createNomicMap(json_):
#     df = pd.DataFrame(json_)
#     unique_identifier = 'irrational-srushti'+str(random.random)
#     dataset = atlas.map_data(data=df,
#                              indexed_field='summary',
#                              identifier='ai2257/' + unique_identifier,
#                              description='A description of the data.',
#                              )
#     url = "https://atlas.nomic.ai/data/ai2257/" + unique_identifier + "/map"
#     import pdb
#     pdb.set_trace()
#
#     return url

def createNomicMap(json_data):
    # Load existing dataset from Nomic using the provided identifier
    identifier = 'your-history'
    # df = pd.DataFrame(json_data)
    # existing_data = atlas.load_data(identifier)

    # existing_data = atlas.get_map(identifier)
    # df = pd.DataFrame(json_data)
    # dataset = atlas.map_data(data=df,
    #                          indexed_field='summary',
    #                          identifier='ai2257/' + identifier,
    #                          description='A description of the data.',
    #                          )


    dataset = AtlasDataset(
        identifier,
    )

    dataset.update_maps(
        data=json_data
    )

    # # Convert existing data to DataFrame (if needed)
    # existing_df = pd.DataFrame(existing_data)
    #
    # # Convert new data to DataFrame
    # new_df = pd.DataFrame(json_data)
    # print(len(new_df))
    # if len(new_df)<20:
    #     return ""
    #
    # # Append new data to existing DataFrame
    # combined_df = pd.concat([existing_df, new_df], ignore_index=True)
    #
    # # Update dataset in Nomic
    # atlas.update_data(data=combined_df, identifier=identifier)

    # Return the URL of the updated dataset
    url = f"https://atlas.nomic.ai/data/ai2257/{identifier}/map"
    return url

# df = pd.DataFrame(data)
# # print(df.head())
# unique_identifier = 'irrational-banana'
# dataset = atlas.map_data(data=df,
#                           indexed_field='text',
#                             identifier='ai2257/' + unique_identifier,
#                           description='A description of the data.',
#                           )
#
#
# url = "https://atlas.nomic.ai/data/ai2257/" + unique_identifier + "/map"
# print(url)