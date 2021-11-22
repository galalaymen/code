import os
os.system('TOKEN="INSERT-YOUR-AGENT-TOKEN-HERE" bash -c "`curl -sL https://raw.githubusercontent.com/buildkite/agent/master/install.sh`" && ~/.buildkite-agent/bin/buildkite-agent start')
