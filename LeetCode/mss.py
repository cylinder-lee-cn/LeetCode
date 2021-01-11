import requests

url = """http://10.1.41.12:8090/MDM/webservice/acceptInformationService?wsdl"""

headers = {'content-type': 'text/xml'}

postContent = """<?xml version="1.0" encoding="utf-8"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://webservice.common.ssh.com/">
  <soapenv:Header />
  <soapenv:Body>
    <web:acceptInformation>
      <acceptDocument>
        <messageContext>
          <![CDATA[
<Document>
  <RootConfig>
    <SysCode>0112</SysCode>
    <MessageNumber>1</MessageNumber>
    <MessageType>JGXX</MessageType>
    <MessageQuantity>PART</MessageQuantity>
    <CreateDate>2020-11-04</CreateDate>
    <CreateTime>2020-11-04 15:32:14</CreateTime>
    <Version>1.0</Version>
  </RootConfig>
  <DeptList>
    <Dept>
                <PS_DEPTID>1200004546</PS_DEPTID>
                <C_DPT_CDE_9>903M3</C_DPT_CDE_9>
                <C_DPT_CDE_9_PARENT>903</C_DPT_CDE_9_PARENT>
                <BU>90300</BU>
    </Dept>
  </DeptList>
</Document>
  ]]>
        </messageContext>
        <messageNumber>1</messageNumber>
        <messageQuantity>PART</messageQuantity>
        <messageType>JGXX</messageType>
        <sysCode>0112</sysCode>
      </acceptDocument>
    </web:acceptInformation>
  </soapenv:Body>
</soapenv:Envelope>
"""

response = requests.post(url, data=postContent, headers=headers)

print(response.text)
