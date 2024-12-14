FROM python
WORKDIR /mydir
COPY . .
RUN pip install flask && \ 
pip install requests
CMD [ "python","main.py" ]