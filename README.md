# facemap-capsule-template
Base CodeOcean capsule template with a working install of [`MouseLand/facemap`](https://github.com/MouseLand/facemap).


- `facemap[gui]==1.0.4` plus all required dependencies (GUI can't be used, but some dependencies are required for analysis)
- tries to update to the latest version of facemap: you may wish to disable this by deleting `/environment/postInstall` 

---

Developing a capsule in codoecean is a lot like developing in a local git repository: 
- you can clone from a remote (github) to get started
- changes are tracked as commits, with commit messages
- changes can be pushed or pulled from a remote

This template sets up a starting point for processing video data with `facemap`.

## for testing
get up and running quickly by *cloning this repo* in codeocean:
- open codeocean in a new tab [here](https://codeocean.allenneuraldynamics.org/)
- hit the `+` icon (top left) and select `"New Capsule" > "Clone from Git"` and paste the URL for this repo: `https://github.com/AllenNeuralDynamics/facemap-capsule-template`
- the capsule should open at this readme

## for more-permanent, collaborative capsule development
*create a new repo*, which can serve as the remote for one or more capsules:
- open this repository on github [here](https://github.com/AllenNeuralDynamics/facemap-capsule-template)
- hit the big green button to "`Use this template`": a new repo will be created after you decide its name
- follow the cloning instructions as per [`# for testing`](#for-testing), but supply the link to your new repo
- the capsule can now pull changes from github, so you can add or edit your files anywhere, push to github, then pull in codeocean
- to push changes *from* codeocean to github:
    - generate a personal access token for your account in github
    - add it to your account in codeocean
