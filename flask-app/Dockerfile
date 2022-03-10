FROM python:3.6
ENV DATABASE_URI=mysql+pymysql://root:password123@mysql:3306/app-db 
COPY . ./
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]