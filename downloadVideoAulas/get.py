import sys
import requests
import re
import readchar
from urllib import parse
from bs4 import BeautifulSoup

def download_video(url, filename):

  if not ".mp4" in filename:
    filename += ".mp4"

  try:
    r = requests.get(url, stream=True, timeout=5)
    i = 0
    with open(filename, "wb") as f:
      for buff in r.iter_content(chunk_size=1024):
        if buff:
          f.write(buff)
          f.flush()
          if(i%1500 == 0):
            print(".", end="", flush=True)
          i +=1
  except requests.exceptions.Timeout:
    return False
  except requests.exceptions.ConnectionError:
    return False

  return filename if i>0 else False

def find_all_videos(url):
  url_base = "http://eaulas.usp.br"
  link_videos = []

  a = parse.urlsplit(url)
  link_videos.append(url_base + a.path+"?"+a.query)

  r = requests.get(url)
  soup = BeautifulSoup(r.text, "html.parser")
  divs = soup.find_all('div', attrs={'id' : 'area-text-vid'})
  for div in divs:
    links = div.find_all('a')
    for link in links:
      link_videos.append(url_base + link.get('href'))
  return link_videos

def find_mp4_source(url):
  r = requests.get(url)
  soup = BeautifulSoup(r.text, "html.parser")
  try:
    script = str(soup.find_all('script')[42])

    start_string = "url: '"
    end_string = "playerType"

    start_position = script.find(start_string) + len(start_string)
    end_position = script.find(end_string)
  except IndexError:
    return False

  return script[start_position:end_position-5]
  
def handler(array_links):
  fail_downloads = []
  success_downloads = []

  for i in range(len(array_links)):
    params = dict(parse.parse_qsl(parse.urlsplit(array_links[i]).query))
    filename = "aula-{}".format(params['idItem'])
    url = find_mp4_source( array_links[i] )
    if not url:
      print("This is not a valid video")
    else:
      print("Downloading the video {}.mp4".format(filename))
      video = download_video(url, filename)
      if video:
        print("\nDownload complete!")
        success_downloads.append(array_links[i])
      else:
        print("\nFail :/")
        fail_downloads.append(array_links[i])

  print("Execution Complete!")
  print("We have a total of {} successful downloads and {} fails".format(len(success_downloads), len(fail_downloads)))
  print("You can try to check the fail downloads by yourself by going at the URLs in the browser and download it here by typing: script_name.py \"url_link\" where script_name is your python file and url_link (wich must be between quotes) is the link to the video you received")
  print("Do you want to check the list of failed downloads?(Y/N)")

  resp = readchar.readchar()

  if resp.lower() == "y":
    for link in fail_downloads:
      print("URL:")
      print(link)
      print()
    print("Thank you to use our app :)")
  else:
    print("Ok, you chose 'N'...")
    print("Thank you to use our app :)")

def main():
  if len(sys.argv) > 1:
    array_links = []
    for i in range(len(sys.argv)):
      if i > 0:
        array_links.append(sys.argv[i])
    handler(array_links)
  else:
    print("Looking for all videos...")
    array_links = find_all_videos("http://eaulas.usp.br/portal/video.action?idItem=7628")
    print("Found {} videos!".format(len(array_links)))
    handler(array_links)
    

if __name__ == '__main__':
  main()