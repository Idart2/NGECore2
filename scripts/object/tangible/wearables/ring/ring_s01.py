import sys

def setup(core, object):
	return
	
def equip(core, actor, object):

	##Direfate
	if object.getStfName() == ('item_ring_set_bh_utility_b_01_01'):
		core.skillModService.addSkillMod(actor, 'bh_dire_root', 1)
		core.skillModService.addSkillMod(actor, 'bh_dire_snare', 1)
		core.skillModService.addSkillMod(actor, 'fast_attack_line_dm_cc', 2)
		return
		
	##Enforcer
	elif object.getStfName() == ('item_ring_set_bh_dps_01_01'):
		core.skillModService.addSkillMod(actor, 'expertise_action_line_dm', 1)
		core.skillModService.addSkillMod(actor, 'expertise_action_line_dm_crit', 1)
		core.skillModService.addSkillMod(actor, 'expertise_buff_duration_line_bh_return_fire' , 1)
		core.skillModService.addSkillMod(actor, 'expertise_cooldown_line_dm' , 1)
		return
		
	##Frontman
	elif object.getStfName() == ('item_ring_set_commando_utility_a_01_01'):
		core.skillModService.addSkillMod(actor, 'constitution_modified', 20)
		core.skillModService.addSkillMod(actor, 'display_only_block' , 40)
		core.skillModService.addSkillMod(actor, 'combat_block_value' , 50)
		return
	return
	
def unequip(core, actor, object):

	##Direfate
	if object.getStfName() == ('item_ring_set_bh_utility_b_01_01'):
		core.skillModService.deductSkillMod(actor, 'bh_dire_root', 1)
		core.skillModService.deductSkillMod(actor, 'bh_dire_snare', 1)
		core.skillModService.deductSkillMod(actor, 'fast_attack_line_dm_cc', 2)
		return
	
	##Enforcer	
	elif object.getStfName() == ('item_ring_set_bh_dps_01_01'):
		core.skillModService.deductSkillMod(actor, 'expertise_action_line_dm', 1)
		core.skillModService.deductSkillMod(actor, 'expertise_action_line_dm_crit', 1)
		core.skillModService.deductSkillMod(actor, 'expertise_buff_duration_line_bh_return_fire' , 1)
		core.skillModService.deductSkillMod(actor, 'expertise_cooldown_line_dm' , 1)
		return
		
	##Frontman
	elif object.getStfName() == ('item_ring_set_commando_utility_a_01_01'):
		core.skillModService.deductSkillMod(actor, 'constitution_modified', 20)
		core.skillModService.deductSkillMod(actor, 'display_only_block' , 40)
		core.skillModService.deductSkillMod(actor, 'combat_block_value' , 50)
		return
	return

	