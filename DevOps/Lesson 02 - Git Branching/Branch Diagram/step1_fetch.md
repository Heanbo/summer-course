# Step 1: git fetch

Fetch the latest changes from the remote repository.

mermaid
gitGraph
    commit id: "Initial commit"
    commit id: "Main commit 1"
    branch feature-a
    checkout feature-a
    commit id: "Feature commit 1"
    commit id: "Feature commit 2"
    commit id: "Feature commit 3" type: HIGHLIGHT
```

After fetching, main has new commits from remote:

```mermaid
gitGraph
    commit id: "Initial commit"
    commit id: "Main commit 1"
    branch feature-a
    checkout feature-a
    commit id: "Feature commit 1"
    commit id: "Feature commit 2"
    commit id: "Feature commit 3" type: HIGHLIGHT
    checkout main
    commit id: "Main commit 2"
```

**What happened?**
- `git fetch` downloaded the latest commits from the remote repository
- Your local `main` branch now knows about the new commits
- Your `feature-a` branch is still based on the old main
