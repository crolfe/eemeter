from eemeter.parsers import GreenButtonParser

import pytest
from numpy.testing import assert_allclose

@pytest.fixture
def natural_gas_xml(request):
    xml = """ <ns1:feed xmlns:ns0="http://naesb.org/espi" xmlns:ns1="http://www.w3.org/2005/Atom">
	<ns1:id xmlns:ns1="http://www.w3.org/2005/Atom">b3671f5d-447f-4cf5-abc2-87c321c3ac31</ns1:id>
	<ns1:title type="text" xmlns:ns1="http://www.w3.org/2005/Atom">Green Button Usage Feed</ns1:title>
	<ns1:updated xmlns:ns1="http://www.w3.org/2005/Atom">2016-03-15T07:24:21.878Z</ns1:updated>
	<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/Batch/Subscription/REDACTED/UsagePoint/REDACTED" rel="self" xmlns:ns1="http://www.w3.org/2005/Atom"/>
	<ns1:entry xmlns:ns1="http://www.w3.org/2005/Atom">
		<ns1:id xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:idType">f7829ece-9aad-4b72-bbf7-920c585700bf</ns1:id>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/LocalTimeParameters" rel="up" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/LocalTimeParameters/1" rel="self" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:title type="text" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:textType">DST FOR PACIFIC TIMEZONE</ns1:title>
		<ns1:published xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:dateTimeType">2016-03-15T07:24:36.374Z</ns1:published>
		<ns1:updated xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:dateTimeType">2016-03-15T07:24:36.376Z</ns1:updated>
		<ns1:content xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:contentType">
			<ns0:LocalTimeParameters xmlns:ns0="http://naesb.org/espi">
				<ns0:dstEndRule>B40E2000</ns0:dstEndRule>
				<ns0:dstOffset>3600</ns0:dstOffset>
				<ns0:dstStartRule>360E2000</ns0:dstStartRule>
				<ns0:tzOffset>-28800</ns0:tzOffset>
			</ns0:LocalTimeParameters>
		</ns1:content>
	</ns1:entry>
	<ns1:entry xmlns:ns1="http://www.w3.org/2005/Atom">
		<ns1:id xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:idType">e634f65c-16f9-4d5c-8f82-898beb773029</ns1:id>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/ReadingType" rel="up" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/ReadingType/MTY5Om51bGw6ODY0MDA6MQ==" rel="self" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:title type="text" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:textType">Type of Meter Reading Data</ns1:title>
		<ns1:published xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:dateTimeType">2016-03-15T07:24:36.376Z</ns1:published>
		<ns1:updated xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:dateTimeType">2016-03-15T07:24:36.377Z</ns1:updated>
		<ns1:content xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:contentType">
			<ns0:ReadingType xmlns:ns0="http://naesb.org/espi">
				<ns0:accumulationBehaviour>4</ns0:accumulationBehaviour>
				<ns0:commodity>7</ns0:commodity>
				<ns0:dataQualifier>12</ns0:dataQualifier>
				<ns0:defaultQuality>17</ns0:defaultQuality>
				<ns0:flowDirection>1</ns0:flowDirection>
				<ns0:intervalLength>86400</ns0:intervalLength>
				<ns0:kind>12</ns0:kind>
				<ns0:powerOfTenMultiplier>-8</ns0:powerOfTenMultiplier>
				<ns0:timeAttribute>11</ns0:timeAttribute>
				<ns0:uom>169</ns0:uom>
				<ns0:measuringPeriod>4</ns0:measuringPeriod>
			</ns0:ReadingType>
		</ns1:content>
	</ns1:entry>
	<ns1:entry xmlns:ns1="http://www.w3.org/2005/Atom">
		<ns1:id xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:idType">d11d9766-e98f-4203-bcd5-1df8481711c2</ns1:id>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/Subscription/REDACTED/UsagePoint" rel="up" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/Subscription/REDACTED/UsagePoint/REDACTED" rel="self" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/Subscription/REDACTED/UsagePoint/REDACTED/MeterReading" rel="related" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/Subscription/REDACTED/UsagePoint/REDACTED/UsageSummary" rel="related" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/LocalTimeParameters/1" rel="related" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:title type="text" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:textType">Green Button Data File</ns1:title>
		<ns1:published xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:dateTimeType">2016-03-15T07:24:36.424Z</ns1:published>
		<ns1:updated xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:dateTimeType">2016-03-15T07:24:36.426Z</ns1:updated>
		<ns1:content xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:contentType">
			<ns0:UsagePoint xmlns:ns0="http://naesb.org/espi">
				<ns0:ServiceCategory>
					<ns0:kind>1</ns0:kind>
				</ns0:ServiceCategory>
			</ns0:UsagePoint>
		</ns1:content>
	</ns1:entry>
	<ns1:entry xmlns:ns1="http://www.w3.org/2005/Atom">
		<ns1:id xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:idType">9b0826bd-a602-49d9-8253-810d8d51af57</ns1:id>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/Subscription/REDACTED/UsagePoint/REDACTED/MeterReading" rel="up" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/Subscription/REDACTED/UsagePoint/REDACTED/MeterReading/REDACTED" rel="self" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/Subscription/REDACTED/UsagePoint/REDACTED/MeterReading/REDACTED/IntervalBlock" rel="related" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/ReadingType/REDACTED" rel="related" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/LocalTimeParameters/1" rel="related" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:title type="text" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:textType">Green Button Data File</ns1:title>
		<ns1:published xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:dateTimeType">2016-03-15T07:24:36.427Z</ns1:published>
		<ns1:updated xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:dateTimeType">2016-03-15T07:24:36.428Z</ns1:updated>
		<ns1:content xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:contentType">
			<ns0:MeterReading xmlns:ns0="http://naesb.org/espi"/>
		</ns1:content>
	</ns1:entry>
	<ns1:entry xmlns:ns1="http://www.w3.org/2005/Atom">
		<ns1:id xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:idType">32a5c33c-d9e3-468b-933c-165c73d3ba72</ns1:id>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/Subscription/REDACTED/UsagePoint/REDACTED/MeterReading/REDACTED/IntervalBlock" rel="up" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/Subscription/REDACTED/UsagePoint/REDACTED/MeterReading/REDACTED/IntervalBlock/1331794801" rel="self" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:title type="text" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:textType">IntervalBlock_1331794801</ns1:title>
		<ns1:published xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:dateTimeType">2016-03-15T07:24:36.429Z</ns1:published>
		<ns1:updated xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:dateTimeType">2016-03-15T07:24:36.429Z</ns1:updated>
		<ns1:content xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:contentType">
			<ns0:IntervalBlock xmlns:ns0="http://naesb.org/espi">
				<ns0:interval>
					<ns0:duration>86400</ns0:duration>
					<ns0:start>1331794801</ns0:start>
				</ns0:interval>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>17</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>86400</ns0:duration>
						<ns0:start>1331794801</ns0:start>
					</ns0:timePeriod>
					<ns0:value>103659540</ns0:value>
				</ns0:IntervalReading>
			</ns0:IntervalBlock>
		</ns1:content>
	</ns1:entry>
	<ns1:entry xmlns:ns1="http://www.w3.org/2005/Atom">
		<ns1:id xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:idType">f710072a-1d0b-4a7a-ab6b-6e1ed368b1cc</ns1:id>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/Subscription/REDACTED/UsagePoint/REDACTED/MeterReading/REDACTED/IntervalBlock" rel="up" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/Subscription/REDACTED/UsagePoint/REDACTED/MeterReading/REDACTED/IntervalBlock/1331881201" rel="self" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:title type="text" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:textType">IntervalBlock_1331881201</ns1:title>
		<ns1:published xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:dateTimeType">2016-03-15T07:24:36.43Z</ns1:published>
		<ns1:updated xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:dateTimeType">2016-03-15T07:24:36.431Z</ns1:updated>
		<ns1:content xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:contentType">
			<ns0:IntervalBlock xmlns:ns0="http://naesb.org/espi">
				<ns0:interval>
					<ns0:duration>86400</ns0:duration>
					<ns0:start>1331881201</ns0:start>
				</ns0:interval>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>17</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>86400</ns0:duration>
						<ns0:start>1331881201</ns0:start>
					</ns0:timePeriod>
					<ns0:value>103659540</ns0:value>
				</ns0:IntervalReading>
			</ns0:IntervalBlock>
		</ns1:content>
	</ns1:entry>
</ns1:feed>"""

    return xml

@pytest.fixture
def electricity_xml():
    xml ="""
<ns1:feed xmlns:ns0="http://naesb.org/espi" xmlns:ns1="http://www.w3.org/2005/Atom">
	<ns1:id xmlns:ns1="http://www.w3.org/2005/Atom">bf2d574c-4f27-4c48-9a49-af418e6c0a7f</ns1:id>
	<ns1:title type="text" xmlns:ns1="http://www.w3.org/2005/Atom">Green Button Usage Feed</ns1:title>
	<ns1:updated xmlns:ns1="http://www.w3.org/2005/Atom">2016-03-15T07:24:56.097Z</ns1:updated>
	<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/Batch/Subscription/REDACTED/UsagePoint/REDACTED" rel="self" xmlns:ns1="http://www.w3.org/2005/Atom"/>
	<ns1:entry xmlns:ns1="http://www.w3.org/2005/Atom">
		<ns1:id xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:idType">1fb4f4e7-031a-40af-931f-4a71e858e7e0</ns1:id>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/LocalTimeParameters" rel="up" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/LocalTimeParameters/1" rel="self" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:title type="text" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:textType">DST FOR PACIFIC TIMEZONE</ns1:title>
		<ns1:published xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:dateTimeType">2016-03-15T07:24:56.095Z</ns1:published>
		<ns1:updated xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:dateTimeType">2016-03-15T07:24:56.096Z</ns1:updated>
		<ns1:content xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:contentType">
			<ns0:LocalTimeParameters xmlns:ns0="http://naesb.org/espi">
				<ns0:dstEndRule>B40E2000</ns0:dstEndRule>
				<ns0:dstOffset>3600</ns0:dstOffset>
				<ns0:dstStartRule>360E2000</ns0:dstStartRule>
				<ns0:tzOffset>-28800</ns0:tzOffset>
			</ns0:LocalTimeParameters>
		</ns1:content>
	</ns1:entry>
	<ns1:entry xmlns:ns1="http://www.w3.org/2005/Atom">
		<ns1:id xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:idType">80dd7c14-73bd-42bd-80b0-602d9d3339ac</ns1:id>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/ReadingType" rel="up" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/ReadingType/NzI6bnVsbDozNjAwOjE=" rel="self" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:title type="text" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:textType">Type of Meter Reading Data</ns1:title>
		<ns1:published xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:dateTimeType">2016-03-15T07:24:56.098Z</ns1:published>
		<ns1:updated xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:dateTimeType">2016-03-15T07:24:56.099Z</ns1:updated>
		<ns1:content xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:contentType">
			<ns0:ReadingType xmlns:ns0="http://naesb.org/espi">
				<ns0:accumulationBehaviour>4</ns0:accumulationBehaviour>
				<ns0:commodity>1</ns0:commodity>
				<ns0:dataQualifier>12</ns0:dataQualifier>
				<ns0:defaultQuality>17</ns0:defaultQuality>
				<ns0:flowDirection>1</ns0:flowDirection>
				<ns0:intervalLength>3600</ns0:intervalLength>
				<ns0:kind>12</ns0:kind>
				<ns0:powerOfTenMultiplier>-3</ns0:powerOfTenMultiplier>
				<ns0:timeAttribute>0</ns0:timeAttribute>
				<ns0:uom>72</ns0:uom>
				<ns0:measuringPeriod>7</ns0:measuringPeriod>
			</ns0:ReadingType>
		</ns1:content>
	</ns1:entry>
	<ns1:entry xmlns:ns1="http://www.w3.org/2005/Atom">
		<ns1:id xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:idType">dce6e5b1-d0e3-4402-abbd-a2b833117ba9</ns1:id>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/Subscription/REDACTED/UsagePoint" rel="up" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/Subscription/REDACTED/UsagePoint/REDACTED" rel="self" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/Subscription/REDACTED/UsagePoint/REDACTED/MeterReading" rel="related" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/Subscription/REDACTED/UsagePoint/REDACTED/UsageSummary" rel="related" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/LocalTimeParameters/1" rel="related" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:title type="text" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:textType">Green Button Data File</ns1:title>
		<ns1:published xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:dateTimeType">2016-03-15T07:24:56.308Z</ns1:published>
		<ns1:updated xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:dateTimeType">2016-03-15T07:24:56.309Z</ns1:updated>
		<ns1:content xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:contentType">
			<ns0:UsagePoint xmlns:ns0="http://naesb.org/espi">
				<ns0:ServiceCategory>
					<ns0:kind>0</ns0:kind>
				</ns0:ServiceCategory>
			</ns0:UsagePoint>
		</ns1:content>
	</ns1:entry>
	<ns1:entry xmlns:ns1="http://www.w3.org/2005/Atom">
		<ns1:id xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:idType">13d5f491-cdc4-4969-a7dd-801ffb317065</ns1:id>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/Subscription/REDACTED/UsagePoint/REDACTED/MeterReading" rel="up" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/Subscription/REDACTED/UsagePoint/REDACTED/MeterReading/REDACTED" rel="self" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/Subscription/REDACTED/UsagePoint/REDACTED/MeterReading/REDACTED/IntervalBlock" rel="related" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/ReadingType/NzI6bnVsbDozNjAwOjE=" rel="related" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/LocalTimeParameters/1" rel="related" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:title type="text" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:textType">Green Button Data File</ns1:title>
		<ns1:published xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:dateTimeType">2016-03-15T07:24:56.311Z</ns1:published>
		<ns1:updated xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:dateTimeType">2016-03-15T07:24:56.311Z</ns1:updated>
		<ns1:content xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:contentType">
			<ns0:MeterReading xmlns:ns0="http://naesb.org/espi"/>
		</ns1:content>
	</ns1:entry>
	<ns1:entry xmlns:ns1="http://www.w3.org/2005/Atom">
		<ns1:id xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:idType">87364635-8071-4f2c-bbf4-6ff9fa8bd7ed</ns1:id>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/Subscription/REDACTED/UsagePoint/REDACTED/MeterReading/REDACTED/IntervalBlock" rel="up" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/Subscription/REDACTED/UsagePoint/REDACTED/MeterReading/REDACTED/IntervalBlock/1331794800" rel="self" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:title type="text" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:textType">IntervalBlock_1331794800</ns1:title>
		<ns1:published xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:dateTimeType">2016-03-15T07:24:56.312Z</ns1:published>
		<ns1:updated xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:dateTimeType">2016-03-15T07:24:56.313Z</ns1:updated>
		<ns1:content xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:contentType">
			<ns0:IntervalBlock xmlns:ns0="http://naesb.org/espi">
				<ns0:interval>
					<ns0:duration>86400</ns0:duration>
					<ns0:start>1331794800</ns0:start>
				</ns0:interval>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331794800</ns0:start>
					</ns0:timePeriod>
					<ns0:value>192200</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331798400</ns0:start>
					</ns0:timePeriod>
					<ns0:value>171100</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331802000</ns0:start>
					</ns0:timePeriod>
					<ns0:value>163500</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331805600</ns0:start>
					</ns0:timePeriod>
					<ns0:value>251900</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331809200</ns0:start>
					</ns0:timePeriod>
					<ns0:value>294000</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331812800</ns0:start>
					</ns0:timePeriod>
					<ns0:value>354600</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331816400</ns0:start>
					</ns0:timePeriod>
					<ns0:value>277900</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331820000</ns0:start>
					</ns0:timePeriod>
					<ns0:value>269300</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331823600</ns0:start>
					</ns0:timePeriod>
					<ns0:value>390200</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331827200</ns0:start>
					</ns0:timePeriod>
					<ns0:value>835600</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331830800</ns0:start>
					</ns0:timePeriod>
					<ns0:value>761100</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331834400</ns0:start>
					</ns0:timePeriod>
					<ns0:value>666400</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331838000</ns0:start>
					</ns0:timePeriod>
					<ns0:value>548800</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331841600</ns0:start>
					</ns0:timePeriod>
					<ns0:value>550200</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331845200</ns0:start>
					</ns0:timePeriod>
					<ns0:value>334600</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331848800</ns0:start>
					</ns0:timePeriod>
					<ns0:value>299400</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331852400</ns0:start>
					</ns0:timePeriod>
					<ns0:value>363500</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331856000</ns0:start>
					</ns0:timePeriod>
					<ns0:value>464500</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331859600</ns0:start>
					</ns0:timePeriod>
					<ns0:value>652900</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331863200</ns0:start>
					</ns0:timePeriod>
					<ns0:value>1441300</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331866800</ns0:start>
					</ns0:timePeriod>
					<ns0:value>2810700</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331870400</ns0:start>
					</ns0:timePeriod>
					<ns0:value>683400</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331874000</ns0:start>
					</ns0:timePeriod>
					<ns0:value>2251400</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331877600</ns0:start>
					</ns0:timePeriod>
					<ns0:value>173400</ns0:value>
				</ns0:IntervalReading>
			</ns0:IntervalBlock>
		</ns1:content>
	</ns1:entry>
	<ns1:entry xmlns:ns1="http://www.w3.org/2005/Atom">
		<ns1:id xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:idType">c1814f4a-6cf4-46a7-ba8a-f55f6cb8a32e</ns1:id>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/Subscription/REDACTED/UsagePoint/REDACTED/MeterReading/REDACTED/IntervalBlock" rel="up" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:link href="https://api.pge.com/GreenButtonConnect/espi/1_1/resource/Subscription/REDACTED/UsagePoint/REDACTED/MeterReading/REDACTED/IntervalBlock/1331881200" rel="self" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:linkType"/>
		<ns1:title type="text" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:textType">IntervalBlock_1331881200</ns1:title>
		<ns1:published xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:dateTimeType">2016-03-15T07:24:56.314Z</ns1:published>
		<ns1:updated xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:dateTimeType">2016-03-15T07:24:56.315Z</ns1:updated>
		<ns1:content xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns1:contentType">
			<ns0:IntervalBlock xmlns:ns0="http://naesb.org/espi">
				<ns0:interval>
					<ns0:duration>86400</ns0:duration>
					<ns0:start>1331881200</ns0:start>
				</ns0:interval>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331881200</ns0:start>
					</ns0:timePeriod>
					<ns0:value>217000</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331884800</ns0:start>
					</ns0:timePeriod>
					<ns0:value>173800</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331888400</ns0:start>
					</ns0:timePeriod>
					<ns0:value>164100</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331892000</ns0:start>
					</ns0:timePeriod>
					<ns0:value>209600</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331895600</ns0:start>
					</ns0:timePeriod>
					<ns0:value>161100</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331899200</ns0:start>
					</ns0:timePeriod>
					<ns0:value>336300</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331902800</ns0:start>
					</ns0:timePeriod>
					<ns0:value>308800</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331906400</ns0:start>
					</ns0:timePeriod>
					<ns0:value>271600</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331910000</ns0:start>
					</ns0:timePeriod>
					<ns0:value>605000</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331913600</ns0:start>
					</ns0:timePeriod>
					<ns0:value>273300</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331917200</ns0:start>
					</ns0:timePeriod>
					<ns0:value>240500</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331920800</ns0:start>
					</ns0:timePeriod>
					<ns0:value>1196000</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331924400</ns0:start>
					</ns0:timePeriod>
					<ns0:value>3798400</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331928000</ns0:start>
					</ns0:timePeriod>
					<ns0:value>3276400</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331931600</ns0:start>
					</ns0:timePeriod>
					<ns0:value>2394800</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331935200</ns0:start>
					</ns0:timePeriod>
					<ns0:value>4589400</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331938800</ns0:start>
					</ns0:timePeriod>
					<ns0:value>392500</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331942400</ns0:start>
					</ns0:timePeriod>
					<ns0:value>420100</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331946000</ns0:start>
					</ns0:timePeriod>
					<ns0:value>222000</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331949600</ns0:start>
					</ns0:timePeriod>
					<ns0:value>327400</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331953200</ns0:start>
					</ns0:timePeriod>
					<ns0:value>343700</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331956800</ns0:start>
					</ns0:timePeriod>
					<ns0:value>323100</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331960400</ns0:start>
					</ns0:timePeriod>
					<ns0:value>266100</ns0:value>
				</ns0:IntervalReading>
				<ns0:IntervalReading>
					<ns0:ReadingQuality>
						<ns0:quality>19</ns0:quality>
					</ns0:ReadingQuality>
					<ns0:timePeriod>
						<ns0:duration>3600</ns0:duration>
						<ns0:start>1331964000</ns0:start>
					</ns0:timePeriod>
					<ns0:value>228000</ns0:value>
				</ns0:IntervalReading>
			</ns0:IntervalBlock>
		</ns1:content>
	</ns1:entry>
</ns1:feed>"""

    return xml

@pytest.fixture
def natural_gas_parser(natural_gas_xml):
    return GreenButtonParser(natural_gas_xml)

@pytest.fixture
def electricity_parser(electricity_xml):
    return GreenButtonParser(electricity_xml)

def test_green_button_parser_get_id_element(natural_gas_parser):
    id_element = natural_gas_parser.get_id_element()
    assert id_element.text == "b3671f5d-447f-4cf5-abc2-87c321c3ac31"

def test_green_button_parser_get_title_element(natural_gas_parser):
    title_element = natural_gas_parser.get_title_element()
    assert title_element.text == "Green Button Usage Feed"

def test_green_button_parser_get_updated_element(natural_gas_parser):
    updated_element = natural_gas_parser.get_updated_element()
    assert updated_element.text == "2016-03-15T07:24:21.878Z"

def test_green_button_parser_get_link_element(natural_gas_parser):
    link_element = natural_gas_parser.get_link_element()
    assert link_element.get("href") == "https://api.pge.com/GreenButtonConnect/espi/1_1/resource/Batch/Subscription/REDACTED/UsagePoint/REDACTED"

def test_green_button_parser_get_entry_elements(natural_gas_parser):
    entry_elements = natural_gas_parser.get_entry_elements()
    assert len(entry_elements) == 6
    assert entry_elements[0].tag == "{http://www.w3.org/2005/Atom}entry"

def test_local_time_parameters(natural_gas_parser):
    local_time_parameters_entry_element = natural_gas_parser.get_local_time_parameters_entry_element()
    timezone = natural_gas_parser.parse_local_time_parameters_entry(local_time_parameters_entry_element)
    assert timezone.zone == "US/Pacific"

def test_reading_types(natural_gas_parser):
    reading_type_entry_elements = natural_gas_parser.get_reading_type_entry_elements()
    reading_type_entry_element = reading_type_entry_elements[0]
    reading_type_data = natural_gas_parser.parse_reading_type_entry(reading_type_entry_element)
    assert reading_type_data["accumulation_behavior"] == "deltaData"
    assert reading_type_data["data_qualifier"] == "normal"
    assert reading_type_data["interval_length"].days == 1
    assert reading_type_data["flow_direction"] == "forward"
    assert reading_type_data["kind"] == "energy"
    assert reading_type_data["time_attribute"] == None
    assert reading_type_data["commodity"] == "naturalGas"
    assert reading_type_data["measuring_period"] == "twentyfourHour"
    assert reading_type_data["power_of_ten_multiplier"] == -8
    assert reading_type_data["default_quality"] == "validated"
    assert reading_type_data["uom"] == "therm"

def test_get_usage_point_entry_element(natural_gas_parser):
    usage_point_entry_element = natural_gas_parser.get_usage_point_entry_element()
    assert usage_point_entry_element.tag == "{http://www.w3.org/2005/Atom}entry"

def test_get_meter_reading_entry_element(natural_gas_parser):
    meter_reading_entry_element = natural_gas_parser.get_meter_reading_entry_element()
    assert meter_reading_entry_element.tag == "{http://www.w3.org/2005/Atom}entry"

def test_get_interval_block_entry_elements(natural_gas_parser):
    entry_elements = natural_gas_parser.get_interval_block_entry_elements()
    assert len(entry_elements) == 2
    assert entry_elements[0].tag == "{http://www.w3.org/2005/Atom}entry"

def test_get_usage_summary_entry_elements(natural_gas_parser):
    entry_elements = natural_gas_parser.get_usage_summary_entry_elements()
    assert len(entry_elements) == 0

def test_get_interval_block_data(natural_gas_parser):
    data = natural_gas_parser.get_interval_block_data()
    assert len(data) == 2
    interval_block_data = data[0]
    assert interval_block_data["interval"]["duration"].days == 1
    assert interval_block_data["interval"]["start"].tzinfo.zone == "US/Pacific"
    assert interval_block_data["reading_type"]["uom"] == "therm"

    interval_reading_data = interval_block_data["interval_readings"][0]
    assert interval_reading_data["duration"].days == 1
    assert interval_reading_data["reading_quality"] == "validated"
    assert interval_reading_data["value"] == 103659540
    assert interval_reading_data["start"].tzinfo.zone == "US/Pacific"

def test_get_consumption_records(natural_gas_parser):
    records = natural_gas_parser.get_consumption_records()
    assert len(records) == 2
    record = records[0]

    assert record['unit_name'] == 'therm'
    assert record['end'].tzinfo.zone == 'US/Pacific'
    assert record['start'].tzinfo.zone == 'US/Pacific'
    assert record['fuel_type'] == 'natural_gas'
    assert_allclose(record['value'], 1.0365954, rtol=1e-3, atol=1e-3)
    assert record['estimated'] == False

def test_get_consumption_data_objects(natural_gas_parser):
    cds = natural_gas_parser.get_consumption_data_objects()
    assert len(cds) == 1
    cd = cds[0]
    assert_allclose(cd.data[0], 1.0365954, rtol=1e-3, atol=1e-3)
    assert_allclose(cd.estimated[0], False, rtol=1e-3, atol=1e-3)
    assert cd.fuel_type == "natural_gas"
    assert cd.unit_name == "therm"

def test_get_consumption_data_objects(electricity_parser):
    cds = electricity_parser.get_consumption_data_objects()
    assert len(cds) == 1
    cd = cds[0]
    assert_allclose(cd.data[0], 192.2, rtol=1e-3, atol=1e-3)
    assert_allclose(cd.estimated[0], False, rtol=1e-3, atol=1e-3)
    assert cd.fuel_type == "electricity"
    assert cd.unit_name == "Wh"
