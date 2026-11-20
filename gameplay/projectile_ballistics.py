import math

def lag_compensate(target_pos, target_vel, latency):
    """延迟回滚。"""
    raise NotImplementedError("TODO: lag_compensate")

def penetration_loss(thickness, angle_cos, base):
    """穿透衰减。"""
    raise NotImplementedError("TODO: penetration_loss")

def substep_count(speed, dt, radius):
    """固定子步。"""
    raise NotImplementedError("TODO: substep_count")

def gravity_drop(t, gravity):
    """重力下坠。"""
    raise NotImplementedError("TODO: gravity_drop")

def layer_order(shield_layer, body_layer):
    """碰撞层排序。"""
    raise NotImplementedError("TODO: layer_order")

def spread_order(pellets):
    """霰弹稳定顺序。"""
    raise NotImplementedError("TODO: spread_order")

def rollback_state(health, destroyed):
    """可破坏物回滚。"""
    raise NotImplementedError("TODO: rollback_state")

def platform_local_velocity(world_vel, platform_vel):
    """平台局部速度。"""
    raise NotImplementedError("TODO: platform_local_velocity")

def path_hash(points):
    """穿透路径哈希。"""
    raise NotImplementedError("TODO: path_hash")

def bullet_id(shooter, shot_index):
    """子弹唯一 id。"""
    raise NotImplementedError("TODO: bullet_id")

def hit_time(distance, speed):
    """命中时间。"""
    raise NotImplementedError("TODO: hit_time")

def pierce_budget(thickness, budget):
    """穿透预算。"""
    raise NotImplementedError("TODO: pierce_budget")

def angle_cos(dx, dy):
    """入射角余弦。"""
    raise NotImplementedError("TODO: angle_cos")

def trajectory_step(position, velocity, dt, gravity):
    """弹道积分。"""
    raise NotImplementedError("TODO: trajectory_step")

def duplicate_guard(seen, bullet_id):
    """重复结算保护。"""
    raise NotImplementedError("TODO: duplicate_guard")
