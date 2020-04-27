#!/usr/bin/env bash
echo ''
echo 磁盘使用情况:
df -h |head -2
echo ''
echo 内存使用情况:
free -h |head -2
echo ''
echo 应用运行情况:
docker stats --no-stream --format "table {{.Container}}\t{{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}" |grep -E "bin|sword"
echo ''
echo 过滤应用错误日志情况:
docker ps |grep -E "bin|sword" |awk  '{print "\n"$2"\n========================";system("docker logs --tail 500 "$1" | grep ERROR |head -5")}'

