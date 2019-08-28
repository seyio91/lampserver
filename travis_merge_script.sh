if [ "$TRAVIS_BRANCH" != "infradev" ]; then 
    exit 0;
fi
export GIT_COMMITTER_EMAIL="seyi_obaweya@yahoo.com"
export GIT_COMMITTER_NAME="Seyi Obaweya"
git config --add remote.origin.fetch +refs/heads/*:refs/remotes/origin/* || exit
git fetch --all || exit
git checkout master || exit
git merge --no-ff "$TRAVIS_COMMIT" || exit
git push https://${GITHUB_TOKEN}@github.com/seyio91/lampserver.git