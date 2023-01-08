# generate_literature__in_Obsidian
Generates an Obsidian note that corresponds to a literature file (such as a .pdf article) and uses custom fields


# What you'll need

## Start with Obsidian

1. Install: Go to https://obsidian.md/ and download the free software
2. Create vault (see the instructions in their website)

## Create a separate note file

1. Copy and paste the following text to a new note:

```
pub:: [[p1]]
path:: C:\Users\UserName\...\LiteratureFolders

[👉🏼 generate_pub_md](<file:///C:\Users\UserName\...\generate_literature_md.py>)
```
2. Rename that note using name:
- "CMD__GET_PUB.md" or
- a name of your choosing, but then you will have to change the corresponding name into the python script


3. Change the data that you copied (from the 1 step of this subsection) so that they correspond to your paths

## Make sure that ...

1. The script's PATH is a higher level path than the Literature Path






