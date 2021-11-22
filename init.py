import os
os.system('rm install.sh')
os.system('TOKEN="fe49bad4265a9cc7a2d27a56eac4f262bfd3c92c37c55e6a16" bash -c "`curl -sL https://raw.githubusercontent.com/buildkite/agent/master/install.sh`"')
os.system('~/.buildkite-agent/bin/buildkite-agent start')
