from api.models import Block

obj = Block.block_manager.create_initial_block()
obj.make_own_hash()
