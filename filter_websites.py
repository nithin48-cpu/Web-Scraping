# import requests
# import re
#
# user = input("Enter the image name : ")
#
# url = f"https://www.google.com/search?q={user}&sxsrf=APwXEdf7QfpWmsMdPz9dMO5PhbAvXTEdyQ:1685794564328&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjIyq6Riqf_AhX3d2wGHfkXD0cQ_AUoAXoECAEQAw&biw=1422&bih=632&dpr=1.35"
#
# user_agent = {
#     'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
# }
#
# response = requests.get(url=url, headers=user_agent).text
# # print(response)
# pattern = "\[\"https://.*\.jpg\",\d+,\d+]"
# # pattern= '\^["'
# images = re.findall(pattern, response)
#
# for image in images:
#     print(image)


# ["https://resize.indiatvnews.com/en/resize/newbucket/400_-/2023/01/re-himalayan-1673008863.jpg",225,400]
# ["https://post.medicalnewstoday.com/wp-content/uploads/sites/3/2020/02/326012_1100-800x825.jpg",825,800]



import requests
import re
user = input("Enter the image name: ")
url = f"https://www.google.com/search?q={user}&sxsrf=APwXEdf7QfpWmsMdPz9dMO5PhbAvXTEdyQ:1685794564328&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjIyq6Riqf_AhX3d2wGHfkXD0cQ_AUoAXoECAEQAw&biw=1422&bih=632&dpr=1.35"
user_agent = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
response = requests.get(url=url, headers=user_agent).text
pattern = "\[\"(https://.*\.jpg)\",\d+,\d+\]"
images = re.findall(pattern, response)
filtered_images = [image for image in images if 'http' in image]
for image in filtered_images:
    print(image)


