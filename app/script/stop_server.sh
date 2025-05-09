pid=$(ps -ef | grep main.py | grep -v grep | awk '{print $2}')
if [ -n "$pid" ]; then
    echo "找到进程，进程ID为: $pid，正在杀掉该进程..."
    kill -9 $pid
    echo "已成功杀掉进程 $pid"
else
    echo "未找到名为 main.py 的进程"
fi
