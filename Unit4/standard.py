"""
You're curating a large collection of NFTs for a digital art gallery, and your first task is to extract the names of these NFTs from a given list of dictionaries. Each dictionary in the list represents an NFT, and contains information such as the name, creator, and current value.

Write the extract_nft_names() function, which takes in this list and returns a list of all NFT names.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

Input: list (of dictionaries representing NFT's and their information)
Output: list (containing names of each NFT)
Constraints: 
Edge Cases:
  - Empty list: return empty list 

Plan: 
Initliaze empty list to store results

for nft in nft_colletion: 
  add name of each nft to results

return results

This will result in a time complexity of O(n) and space complexity O(n)
"""

def extract_nft_names(nft_collection):
  nft_names = []

  for nft in nft_collection:
    nft_names.append(nft["name"])

  return nft_names

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Future City", "creator": "UrbanArt", "value": 3.8}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

# print(extract_nft_names(nft_collection))
# print(extract_nft_names(nft_collection_2))
# print(extract_nft_names(nft_collection_3))

"""
NFT Collection Review:

You're responsible for ensuring the quality of the NFT collection before it is displayed in the virtual gallery. One of your tasks is to review and debug the code that extracts the names of NFTs from the collection. A junior developer wrote the initial version of this function, but it contains some bugs that prevent it from working correctly.

There is an error in the for loop where we are not correctly appending to the the nft_names list. 
"""

def extract_nft_names(nft_collection):
    nft_names = []
    for nft in nft_collection:
        nft_names.append(nft["name"])
    return nft_names

# print(extract_nft_names(nft_collection))
# print(extract_nft_names(nft_collection_2))
# print(extract_nft_names(nft_collection_3))

"""
Input: list (of dictionaries representing NFT information)
Output: list (of popular creators)
Constraints: creators are popular if they have created more than one nft 
Edge Cases: 
  - All creators have one nft: return empty list 
  - Empty nft collection: return empty list 

Plan: 
Initialize a dict to keep track of the names of creators
Initialize a list to keep track of popular creators

for nft in nft_collection:
  if nft not in dict:
    add nft to the dict with a value of 1
  elif nft has not occured more than 2 times:
    add nft to the popular creators list

return list of popular creators

Time and Complexity: 
Time: O(n) because we are looping through the nft_collection, where the collection has n items 
Space: O(n) because we can have a worst case scenerio of the set being the same length of the nft_collection
"""

def identify_popular_creators(nft_collection):
  occurences = {}
  popularCreators = []

  for nft in nft_collection:
    occurences[nft["creator"]] = occurences.get(nft["creator"], 0) + 1

    if occurences[nft["creator"]] == 2: 
       popularCreators.append(nft["creator"])

  return popularCreators

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

# print(identify_popular_creators(nft_collection))
# print(identify_popular_creators(nft_collection_2))
# print(identify_popular_creators(nft_collection_3))
       
"""
Iput: list (collection of nfts and their information)
Output: integer (average value of the nft's in the collection)
Constraints: 
  - every nft has a value
Edge:
  - empty list: average  = 0

Plan: 
Initialize totalValue variable to keep track of value of nft's 

for nft in the nft_collection:
  add the nft value to the totalValue variable

return totalValue / len(nft_collection) 

Time and Space Complexity: 
Time: O(n) because we are looping through each element in the nft collection
Space: O(1) because we are only using one variable to keep track of the total 
"""

def average_nft_value(nft_collection):
  totalVal = 0

  for nft in nft_collection:
     totalVal += nft["value"]

  return 0 if len(nft_collection) == 0 else totalVal / len(nft_collection)

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]
print(average_nft_value(nft_collection))

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
    {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4}
]
print(average_nft_value(nft_collection_2))

nft_collection_3 = []
print(average_nft_value(nft_collection_3))

"""
Input: list (collection of nfts grouped into collections, each collection may contain more than one nft)
Output: list (nfts that have the tag that we are looking for)
Constraints: NFTs are grouped into collections, each NFT may contain more than one NFT 
Edge Cases:
  - empty collection: return empty list 

Plan: 
initialize list to keep track of the nfts with the specified tag

for collection in nft_collection:
  for nft in collection:
    if tag is in the nft["tags"]:
      append nft name to result list

return result list

Time and Space Complexity: 
Time: O(n) beacause we are looping through each element in the collection and going through their tags (finite number that will not exceed n as n approaches infinity)
Space: O(n) beacuse we are initializing a list to store the results
""" 

def search_nft_by_tag(nft_collections, tag):
  tagged_nfts = []

  for collection in nft_collections:
    for nft in collection:
      if tag in nft["tags"]:
        tagged_nfts.append(nft["name"])

  return tagged_nfts

# nft_collections = [
#     [
#         {"name": "Abstract Horizon", "tags": ["abstract", "modern"]},
#         {"name": "Pixel Dreams", "tags": ["pixel", "retro"]}
#     ],
#     [
#         {"name": "Urban Jungle", "tags": ["urban", "landscape"]},
#         {"name": "City Lights", "tags": ["modern", "landscape"]}
#     ]
# ]

# nft_collections_2 = [
#     [
#         {"name": "Golden Hour", "tags": ["sunset", "landscape"]},
#         {"name": "Sunset Serenade", "tags": ["sunset", "serene"]}
#     ],
#     [
#         {"name": "Pixel Odyssey", "tags": ["pixel", "adventure"]}
#     ]
# ]

# nft_collections_3 = [
#     [
#         {"name": "The Last Piece", "tags": ["finale", "abstract"]}
#     ],
#     [
#         {"name": "Ocean Waves", "tags": ["seascape", "calm"]},
#         {"name": "Mountain Peak", "tags": ["landscape", "adventure"]}
#     ]
# ]

# print(search_nft_by_tag(nft_collections, "landscape"))
# print(search_nft_by_tag(nft_collections_2, "sunset"))
# print(search_nft_by_tag(nft_collections_3, "modern"))
     


