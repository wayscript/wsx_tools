from codecs import EncodedFile
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)

import base64

import os

# Data from excel spreadsheet
df = pd.read_excel('SampleReportsData.xlsx')

# Using the Data
print(df.head(5))
grouped_df = df.groupby(['Shift']).sum()
grouped_df = grouped_df.drop(columns=['Employee ID'])

fig = px.bar(grouped_df, x=grouped_df.index, y='Units Produced')
fig.write_image("production_graph.pdf")

"""Build attachment"""
with open('production_graph.pdf', 'rb') as f:
    data = f.read()
    f.close()

encoded_file = base64.b64encode(data).decode()

attachedFile = Attachment(
    FileContent(encoded_file),
    FileName('attachment.pdf'),
    FileType('application/pdf'),
    Disposition('attachment')
)

message = Mail(
    from_email='Derrick+testing2@wayscript.com',
    to_emails='Derrick@wayscript.com',
    subject='Daily Report',
    html_content='Please find attached report')

message.attachment = attachedFile

sg = SendGridAPIClient("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")
response = sg.send(message)
print(response.status_code, response.body, response.headers)