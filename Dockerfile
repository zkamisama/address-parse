# 使用官方Python运行时作为父镜像
FROM python:3.8

# 设置工作目录
WORKDIR /app

# 将本地代码复制到容器中
COPY . /app

# 安装依赖
RUN pip3 install --no-cache-dir jionlp flask addressrec lac

# 使端口5000可供外部访问
EXPOSE 5000

# 定义环境变量
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# 运行flask命令来启动应用程序
CMD ["flask", "run"]