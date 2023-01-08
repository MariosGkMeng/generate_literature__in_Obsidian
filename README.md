# generate_literature__in_Obsidian
Generates an Obsidian note that corresponds to a literature file (such as a .pdf article) and uses custom fields


# What you'll need

## Start with Obsidian

1. Install: Go to https://obsidian.md/ and download the free software
2. Create vault (see the instructions in their website)

## Create a separate note file

1. Copy and paste the following text to a new note (we will call it the "Trigger File"):

```
pub:: [[p1]]
path:: C:\Users\UserName\...\LiteratureFolders

⬇️ Press the button below to generate the literature note-file
[👉🏼 generate_pub_md](<file:///C:\Users\UserName\...\generate_literature_md.py>)
```
2. Rename that note using name:
- "CMD__GET_PUB.md" or
- a name of your choosing, but then you will have to change the corresponding name into the python script


3. Change the data that you copied (from the 1 step of this subsection) so that they correspond to your paths

## Make sure that ...

1. The script's PATH is a higher level path than the Literature Path



# How to use

1. Move your new .pdf (or other readable format) file in your Literature Folder
2. Rename it using the format: str(pdfNumber) + '.' + titleOfArticle + '.pdf', wherein `pdfNumber` is the ascending pdf sequence number (e.g. the 10th pdf you placed in your folder starts with "10. ").
3. Go to Obsidian and open the Trigger File
4. Change the publication number to the `pdfNumber` value (e.g. `pub:: [p10]`)
5. Press the link/button `👉🏼 generate_pub_md`. 
6. Wait for ~1 second
7. Notice that the text "p10" will be available now (the link color is brighter). Click on it
8. That's it! Now you have your literature-note-file, which you can manipulate the way you want



