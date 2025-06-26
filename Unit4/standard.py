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

print(identify_popular_creators(nft_collection))
print(identify_popular_creators(nft_collection_2))
print(identify_popular_creators(nft_collection_3))
       
        

