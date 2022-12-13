FROM python

RUN pip install numexpr colorama && mkdir calc

WORKDIR calc

COPY calc.py .

CMD python calc.py
