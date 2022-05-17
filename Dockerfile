FROM python

WORKDIR /app
# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt .

ENV DB_URL=mysql://admin:Phani_26@terraform-20220517071459810400000001.cjgac39ylraz.us-west-2.rds.amazonaws.com/aws
ENV ACCESS_KEY=AKIA4MC6LBIEHP444GPO
ENV SECRET_KEY=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
#this runs when image is built
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT [ "python" ,"app.py" ]
