FROM python
WORKDIR /mydir
COPY . .
RUN pip install flask && \ 
pip install requests
EXPOSE 5000
CMD [ "python3","main.py" ]