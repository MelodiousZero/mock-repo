# Contributions-Importer-For-Github/run_script.py
import git
from git_contributions_importer import *

# Your private repo or Bitbucket repo
repo = git.Repo(r"C:\Users\llra2001\Documents\GitHub\geo-scan-extractions")
# Your mock repo
mock_repo = git.Repo(r"C:\Users\llra2001\Documents\GitHub\mock-repo")
importer = Importer([repo], mock_repo)
# I use both my personal email and work email here,
# Since the private repo uses work email, and Github uses my personal email
importer.set_author(['raul.llamosas182@gmail.com', 'raul.llamosas@nielseniq.com'])
importer.import_repository()
print("hmouj")
