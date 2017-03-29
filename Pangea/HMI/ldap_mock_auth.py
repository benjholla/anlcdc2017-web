import hashlib

def authenticate(username, password):
  if username == 'f.castle' and sha256(password) == '6da0fdbc8e52df7230532bdad3c12de75035fb84fb7c7b7bdc6c572f84f0347c':
      return True
  elif username == 'l.delrose' and sha256(password) == 'a9f804f256702b75f4e2b0f5fb7b2411e0c1f55bd9dd65a6d5d246cc9f68bcf2':
      return True
  elif username == 'c.wheeler' and sha256(password) == 'baeb0ee6729c771ee68482fcd2b923fb41a4386bf31da3a84d163106574da92c':
      return True
  elif username == 'j.hoyt' and sha256(password) == 'c9caaf0c13d3a48445ae8434b31a06eb46c489903fe80445529d3036d9db2e6e':
      return True
  elif username == 's.wilhelm' and sha256(password) == '451ed06aa704a47db2040d5336dff372da037057dfab4796df9577a40a7b0602':
      return True
  elif username == 'p.emerson' and sha256(password) == '839284d510660a5ab30d31dc06a9fd52e14b84a0052b226c807e6950c9ab16cf':
      return True
  elif username == 'p.luther' and sha256(password) == '631b163b1cbb96add87aff791ccdcf82c066e2f6fe240e193296a88acc7e760c':
      return True
  elif username == 'k.holmes' and sha256(password) == '3f505a2f26b7663ba5936409a07a7adb0365fcc42c1a4d848053dfdc03b46119':
      return True
  elif username == 's.smith' and sha256(password) == '2121b260b1700b7b468bf21204b005f62107f38ef3d37f06f190b8c208280ea0':
      return True
  elif username == 'j.wright' and sha256(password) == '8e4ea90f4958eab01aa937c772cfb97db037f17845d415895b1e3459359613b6':
      return True
  elif username == 't.fritz' and sha256(password) == '0cd80ca15d77f6c0cc179a4b29cbccae4d1edefe7da42e9df3f3372f6c6f3b90':
      return True
  elif username == 'c.licht' and sha256(password) == '1f33eb1586d10793251f27d5e0b851161093c933a0c50e2263177981ef6953ed':
      return True
  elif username == 'h.peterson' and sha256(password) == 'c6805824eb67554cf925a761595fbe876071ff608ce381405a0b9bc1d625e926':
      return True
  elif username == 'b.wells' and sha256(password) == '1c44d10f7f5f5d251354b1beb451aaf6b286964484029aae37e0f3616b817f83':
      return True
  elif username == 's.taylor' and sha256(password) == '7162d5cf377765a4bee3ce0ac9c28793fc76aae1376cdc195b7675a70c5754a0':
      return True
  elif username == 'a.thompson' and sha256(password) == '661699ebe4273f23b67302373a3732792678e003789dca215506da98442a2e45':
      return True
  else:
      return False

def hasMembershipWithSession(username, session, membership):
  if username == "a.thompson" and (membership == "water_tech" or membership == "power_tech"):
      return True
  elif username == "c.licht" and membership == "power_tech":
      return True
  elif username == "t.fritz" and membership == "water_tech":
      return True
  elif username == "j.wright" and membership == "water_tech":
      return True
  else:
      return False
  
def hasMembership(username, password, membership):
  return hasMembershipWithSession(username, None, membership)

def unauthenticate(session):
  return True

def sha256(input):
  return str(hashlib.sha256(input).hexdigest())