def create_pmem_pool(args):
    num_blocks = (args.total_size * 1024 * 1024) / args.block_size
    params = {'pmem_file': args.pmem_file,
              'num_blocks': num_blocks,
              'block_size': args.block_size}
    return args.client.call('create_pmem_pool', params)


def pmem_pool_info(args):
    params = {'pmem_file': args.pmem_file}
    return args.client.call('pmem_pool_info', params)


def delete_pmem_pool(args):
    params = {'pmem_file': args.pmem_file}
    return args.client.call('delete_pmem_pool', params)
