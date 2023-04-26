import git

source_repo = git.Repo('../')
try:
  print(sorted(source_repo.tags,key=lambda t: t.commit.committed_datetime))
  latest_tag=sorted(source_repo.tags,key=lambda t: t.commit.committed_datetime)[-1]
except:
  latest_tag="0.0.1"
print(latest_tag)

destination_repo=git.Repo('.')
new_tag=destination_repo.create_tag(latest_tag)
# destination_repo.git.add(update=True)
# destination_repo.index.commit(f"Automatic build v{new_tag}")
# destination_repo.remotes.origin.push(new_tag)
# destination_repo.remotes.origin.push()
print("Status: ",destination_repo.git.status())
print("Git add: ",destination_repo.git.add(['.']))
print("git commit: ",destination_repo.index.commit(f"Automatic build v{new_tag}"))
print("Taggged: ",destination_repo.remotes.origin.push(new_tag))
print("Active branch: ",destination_repo.active_branch.name)
print("Git pushed: ",destination_repo.remotes.origin.push())

