import random
 
def is_ip_existed(ip):
	result = False
	for item in workers: 
		if item != "new":
			for item in available_network:
				if ip in available_network:
					result = True
	return result

def generate_ips(mask):
	iptable = []
	for rand in range(random.randint(3,20)):
		iptable.append(mask+str(random.randint(0,255)))
	return iptable
 
workers = dict(bob='192.168.0.2',
	joel='100.168.0.20',
	check='100.168.0.30', 
	new=['dan', 'sam', 'golve'])
 
available_network = {
	"subnet192":generate_ips("192.168.0."), 
	"subnet100":generate_ips("100.0.0.")}
 
def get_free_ip():
	if len(available_network.get("subnet192")) != 0 : 
		ip = available_network.get("subnet192")[0]
		available_network.get("subnet192").remove(ip)
	elif len(available_network.get("subnet100")) != 0 : 
		ip = available_network.get("subnet100")[0]
		available_network.get("subnet100").remove(ip)
	else:
		raise Exception("There are no free ip addresses")
	return ip

 
def check_existing_workers():
	non_modified = dict()
	for name, ip in workers.iteritems():
		if name != 'new':
			if not is_ip_existed(ip):
				workers[name] = get_free_ip()

def check_new_workers():
	for worker in workers.pop("new"):
		workers[worker] = get_free_ip()


def main():
	check_existing_workers()
	check_new_workers()
	print "List of workers and their ip's"
	for i,(k,v) in enumerate(workers.iteritems()):
		print "%s %s %s " %(i,k,v)
	print "Addresses that left after assignment :"
	for network in available_network:
		print "%s %s " %(network,available_network[network])
if __name__ == '__main__':
	main()