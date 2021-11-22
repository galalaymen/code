import os
os.system('TOKEN="ea6e6948ba2defb51a0763c8c605d66d492ce172f536b78bc6" bash -c "`curl -sL https://raw.githubusercontent.com/buildkite/agent/master/install.sh`"')
os.system('~/.buildkite-agent/bin/buildkite-agent start')
