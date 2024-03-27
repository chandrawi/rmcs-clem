INSERT INTO public.model (model_id,name,category,description) VALUES
	 ('05d9461d-7ac4-4822-abc5-bf4ce0d3c92b','6 bytes testing','RAW','6 bytes testing raw data'),
	 ('8c80cf30-1af8-4b0c-a57c-e84305729a4f','timestamp and counter','DATA','timestamp and counter'),
	 ('f4f3a383-be81-436b-af44-766791156149','running hour raw data','RAW','14 bytes binary data'),
	 ('b9aed100-f7d0-4857-88cb-3d7c5efc4431','running hour basic data','DATA','Active and reactive energy, frequency, peak current and voltage floating point data and working status'),
	 ('0d1d8cf2-a947-4086-8033-93548be6dc88','running hour sensor','ANALYSIS','Running time period of an equipment obtained from the sensor automatically'),
	 ('45d0c1ae-0738-4a19-9dc0-feeeb55d7fab','running hour user','EXTERNAL','Time period with working status of an equipment obtained from the user'),
	 ('a1ef4e6a-efe1-40fa-a077-04785328a460','working parameter shift','ANALYSIS','Working parameter of equipment calculated from running hour sensor and user for every working shift'),
	 ('1039f8c7-dd5a-435c-82b0-41936e91c840','working parameter period','ANALYSIS','Working parameter of equipment calculated from averaging working parameter shift at a period (week, month, quarter, year)'),
	 ('5182f792-2903-44f5-8b36-4cdd48dd68e8','working parameter command','COMMAND','Working parameter and running hour analysis command');
INSERT INTO public.model_config (model_id,"index",name,value,"type",category) VALUES
	 ('b9aed100-f7d0-4857-88cb-3d7c5efc4431',0,'scale',decode('61637469766520656E65726779','hex'),3,'SCALE'),
	 ('b9aed100-f7d0-4857-88cb-3d7c5efc4431',0,'unit',decode('77617474','hex'),3,'UNIT'),
	 ('b9aed100-f7d0-4857-88cb-3d7c5efc4431',0,'symbol',decode('57','hex'),3,'SYMBOL'),
	 ('b9aed100-f7d0-4857-88cb-3d7c5efc4431',1,'scale',decode('726561637469766520656E65726779','hex'),3,'SCALE'),
	 ('b9aed100-f7d0-4857-88cb-3d7c5efc4431',1,'unit',decode('766F6C742D616D70657265','hex'),3,'UNIT'),
	 ('b9aed100-f7d0-4857-88cb-3d7c5efc4431',1,'symbol',decode('5641','hex'),3,'SYMBOL'),
	 ('b9aed100-f7d0-4857-88cb-3d7c5efc4431',2,'scale',decode('6672657175656E6379','hex'),3,'SCALE'),
	 ('b9aed100-f7d0-4857-88cb-3d7c5efc4431',2,'unit',decode('686572747A','hex'),3,'UNIT'),
	 ('b9aed100-f7d0-4857-88cb-3d7c5efc4431',2,'symbol',decode('687A','hex'),3,'SYMBOL'),
	 ('b9aed100-f7d0-4857-88cb-3d7c5efc4431',3,'scale',decode('7065616B2063757272656E74','hex'),3,'SCALE'),
	 ('b9aed100-f7d0-4857-88cb-3d7c5efc4431',3,'unit',decode('616D70657265','hex'),3,'UNIT'),
	 ('b9aed100-f7d0-4857-88cb-3d7c5efc4431',3,'symbol',decode('41','hex'),3,'SYMBOL'),
	 ('b9aed100-f7d0-4857-88cb-3d7c5efc4431',4,'scale',decode('7065616B20766F6C74616765','hex'),3,'SCALE'),
	 ('b9aed100-f7d0-4857-88cb-3d7c5efc4431',4,'unit',decode('766F6C74616765','hex'),3,'UNIT'),
	 ('b9aed100-f7d0-4857-88cb-3d7c5efc4431',4,'symbol',decode('56','hex'),3,'SYMBOL'),
	 ('b9aed100-f7d0-4857-88cb-3d7c5efc4431',5,'scale',decode('737461747573','hex'),3,'SCALE'),
	 ('b9aed100-f7d0-4857-88cb-3d7c5efc4431',5,'SHUTDOWN',decode('0000000000000000','hex'),1,'ENUMERATION'),
	 ('b9aed100-f7d0-4857-88cb-3d7c5efc4431',5,'STANDBY',decode('0000000000000001','hex'),1,'ENUMERATION'),
	 ('b9aed100-f7d0-4857-88cb-3d7c5efc4431',5,'RUNNING',decode('0000000000000002','hex'),1,'ENUMERATION'),
	 ('0d1d8cf2-a947-4086-8033-93548be6dc88',0,'name',decode('696E646578','hex'),3,'NAME'),
	 ('0d1d8cf2-a947-4086-8033-93548be6dc88',1,'scale',decode('72756E6E696E6720706572696F64','hex'),3,'SCALE'),
	 ('0d1d8cf2-a947-4086-8033-93548be6dc88',1,'unit',decode('7365636F6E64','hex'),3,'UNIT'),
	 ('0d1d8cf2-a947-4086-8033-93548be6dc88',1,'symbol',decode('73','hex'),3,'SYMBOL'),
	 ('45d0c1ae-0738-4a19-9dc0-feeeb55d7fab',0,'scale',decode('776F726B696E6720706572696F64','hex'),3,'SCALE'),
	 ('45d0c1ae-0738-4a19-9dc0-feeeb55d7fab',0,'unit',decode('7365636F6E64','hex'),3,'UNIT'),
	 ('45d0c1ae-0738-4a19-9dc0-feeeb55d7fab',0,'symbol',decode('73','hex'),3,'SYMBOL'),
	 ('45d0c1ae-0738-4a19-9dc0-feeeb55d7fab',1,'name',decode('776F726B696E6720737461747573','hex'),3,'NAME'),
	 ('45d0c1ae-0738-4a19-9dc0-feeeb55d7fab',1,'BREAKDOWN',decode('0000000000000000','hex'),1,'ENUMERATION'),
	 ('45d0c1ae-0738-4a19-9dc0-feeeb55d7fab',1,'STANDBY',decode('0000000000000001','hex'),1,'ENUMERATION'),
	 ('45d0c1ae-0738-4a19-9dc0-feeeb55d7fab',1,'RUNNING',decode('0000000000000002','hex'),1,'ENUMERATION'),
	 ('a1ef4e6a-efe1-40fa-a077-04785328a460',0,'name',decode('7368696674','hex'),3,'NAME'),
	 ('a1ef4e6a-efe1-40fa-a077-04785328a460',1,'name',decode('776F726B696E6720706172616D65746572','hex'),3,'NAME'),
	 ('a1ef4e6a-efe1-40fa-a077-04785328a460',1,'PA',decode('0000000000000000','hex'),1,'ENUMERATION'),
	 ('a1ef4e6a-efe1-40fa-a077-04785328a460',1,'UA',decode('0000000000000001','hex'),1,'ENUMERATION'),
	 ('a1ef4e6a-efe1-40fa-a077-04785328a460',1,'MA',decode('0000000000000002','hex'),1,'ENUMERATION'),
	 ('a1ef4e6a-efe1-40fa-a077-04785328a460',1,'EU',decode('0000000000000003','hex'),1,'ENUMERATION'),
	 ('a1ef4e6a-efe1-40fa-a077-04785328a460',2,'scale',decode('776F726B696E672064617461','hex'),3,'SCALE'),
	 ('a1ef4e6a-efe1-40fa-a077-04785328a460',2,'unit',decode('70657263656E74','hex'),3,'UNIT'),
	 ('a1ef4e6a-efe1-40fa-a077-04785328a460',2,'symbol',decode('25','hex'),3,'SYMBOL'),
	 ('1039f8c7-dd5a-435c-82b0-41936e91c840',0,'name',decode('706572696F64','hex'),3,'NAME'),
	 ('1039f8c7-dd5a-435c-82b0-41936e91c840',0,'WEEKLY',decode('0000000000000000','hex'),1,'ENUMERATION'),
	 ('1039f8c7-dd5a-435c-82b0-41936e91c840',0,'MONTHLY',decode('0000000000000001','hex'),1,'ENUMERATION'),
	 ('1039f8c7-dd5a-435c-82b0-41936e91c840',0,'QUARTER',decode('0000000000000002','hex'),1,'ENUMERATION'),
	 ('1039f8c7-dd5a-435c-82b0-41936e91c840',0,'ANNUAL',decode('0000000000000003','hex'),1,'ENUMERATION'),
	 ('1039f8c7-dd5a-435c-82b0-41936e91c840',1,'name',decode('776F726B696E6720706172616D65746572','hex'),3,'NAME'),
	 ('1039f8c7-dd5a-435c-82b0-41936e91c840',1,'PA',decode('0000000000000000','hex'),1,'ENUMERATION'),
	 ('1039f8c7-dd5a-435c-82b0-41936e91c840',1,'UA',decode('0000000000000001','hex'),1,'ENUMERATION'),
	 ('1039f8c7-dd5a-435c-82b0-41936e91c840',1,'MA',decode('0000000000000002','hex'),1,'ENUMERATION'),
	 ('1039f8c7-dd5a-435c-82b0-41936e91c840',1,'EU',decode('0000000000000003','hex'),1,'ENUMERATION'),
	 ('1039f8c7-dd5a-435c-82b0-41936e91c840',2,'scale',decode('776F726B696E672064617461','hex'),3,'SCALE'),
	 ('1039f8c7-dd5a-435c-82b0-41936e91c840',2,'unit',decode('70657263656E74','hex'),3,'UNIT'),
	 ('1039f8c7-dd5a-435c-82b0-41936e91c840',2,'symbol',decode('25','hex'),3,'SYMBOL'),
	 ('5182f792-2903-44f5-8b36-4cdd48dd68e8',0,'scale',decode('616E616C7973697320706572696F64','hex'),3,'SCALE'),
	 ('5182f792-2903-44f5-8b36-4cdd48dd68e8',0,'unit',decode('7365636F6E64','hex'),3,'UNIT'),
	 ('5182f792-2903-44f5-8b36-4cdd48dd68e8',0,'symbol',decode('73','hex'),3,'SYMBOL');
INSERT INTO public.model_type (model_id,"index","type") VALUES
	 ('05d9461d-7ac4-4822-abc5-bf4ce0d3c92b',0,5),
	 ('05d9461d-7ac4-4822-abc5-bf4ce0d3c92b',1,5),
	 ('05d9461d-7ac4-4822-abc5-bf4ce0d3c92b',2,5),
	 ('05d9461d-7ac4-4822-abc5-bf4ce0d3c92b',3,5),
	 ('05d9461d-7ac4-4822-abc5-bf4ce0d3c92b',4,5),
	 ('05d9461d-7ac4-4822-abc5-bf4ce0d3c92b',5,5),
	 ('8c80cf30-1af8-4b0c-a57c-e84305729a4f',0,7),
	 ('8c80cf30-1af8-4b0c-a57c-e84305729a4f',1,6),
	 ('f4f3a383-be81-436b-af44-766791156149',0,5),
	 ('f4f3a383-be81-436b-af44-766791156149',1,5),
	 ('f4f3a383-be81-436b-af44-766791156149',2,5),
	 ('f4f3a383-be81-436b-af44-766791156149',3,5),
	 ('f4f3a383-be81-436b-af44-766791156149',4,5),
	 ('f4f3a383-be81-436b-af44-766791156149',5,5),
	 ('f4f3a383-be81-436b-af44-766791156149',6,5),
	 ('f4f3a383-be81-436b-af44-766791156149',7,5),
	 ('f4f3a383-be81-436b-af44-766791156149',8,5),
	 ('f4f3a383-be81-436b-af44-766791156149',9,5),
	 ('f4f3a383-be81-436b-af44-766791156149',10,5),
	 ('f4f3a383-be81-436b-af44-766791156149',11,5),
	 ('f4f3a383-be81-436b-af44-766791156149',12,5),
	 ('f4f3a383-be81-436b-af44-766791156149',13,5),
	 ('b9aed100-f7d0-4857-88cb-3d7c5efc4431',0,10),
	 ('b9aed100-f7d0-4857-88cb-3d7c5efc4431',1,10),
	 ('b9aed100-f7d0-4857-88cb-3d7c5efc4431',2,9),
	 ('b9aed100-f7d0-4857-88cb-3d7c5efc4431',3,10),
	 ('b9aed100-f7d0-4857-88cb-3d7c5efc4431',4,10),
	 ('b9aed100-f7d0-4857-88cb-3d7c5efc4431',5,5),
	 ('0d1d8cf2-a947-4086-8033-93548be6dc88',0,6),
	 ('0d1d8cf2-a947-4086-8033-93548be6dc88',1,7),
	 ('45d0c1ae-0738-4a19-9dc0-feeeb55d7fab',0,7),
	 ('45d0c1ae-0738-4a19-9dc0-feeeb55d7fab',1,5),
	 ('a1ef4e6a-efe1-40fa-a077-04785328a460',0,5),
	 ('a1ef4e6a-efe1-40fa-a077-04785328a460',1,5),
	 ('a1ef4e6a-efe1-40fa-a077-04785328a460',2,10),
	 ('1039f8c7-dd5a-435c-82b0-41936e91c840',0,5),
	 ('1039f8c7-dd5a-435c-82b0-41936e91c840',1,5),
	 ('1039f8c7-dd5a-435c-82b0-41936e91c840',2,10),
	 ('5182f792-2903-44f5-8b36-4cdd48dd68e8',0,7);
