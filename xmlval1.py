from xml.dom import minidom

dom = minidom.parse('xmlvalidator.xml')
contract_ids = dom.getElementsByTagName('contract_id')
print(len(contract_ids))
mbr_ids=dom.getElementsByTagName('mbr_id')
mbr_incent_levels=dom.getElementsByTagName('mbr_incent_level')
print(len(mbr_ids))
print(len(mbr_incent_levels))
      
for contract_id,mbr_id,mbr_incent_level in contract_ids,mbr_ids,mbr_incent_levels:
    contractid=[]
    contractid.append(contract_id.firstChild.nodeValue)
    
    mbrid=[]
    mbrid.append(mbr_id.firstChild.nodeValue)

    mbr_incentlevel=[]
    mbr_incentlevel.append(mbr_incent_level.firstChild.nodeValue)
    
    response=(contractid,mbrid,mbr_incentlevel)
    print(response)
    #print(mbrid)
    #print(mbr_incentlevel)

    #print("--------------")
    #print(contractid,mbrid,mbr_incentlevel)

