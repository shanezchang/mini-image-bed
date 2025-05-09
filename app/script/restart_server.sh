pid=$(ps -ef | grep main.py | grep -v grep | awk '{print $2}')
if [ -n "$pid" ]; then
    echo "找到进程，进程ID为: $pid，正在杀掉该进程..."
    kill -9 $pid
    echo "已成功杀掉进程 $pid"
else
    echo "未找到名为 main.py 的进程"
fi
nohup python3 ./app/main.py >> ./app/log/console.log 2>&1 &
echo "main.py 已在后台启动，执行日志将增量写入到 console.log 文件中"
