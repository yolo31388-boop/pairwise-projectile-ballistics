import math


def lag_compensate(target_pos, target_vel, latency):
    """延迟回滚：按开火帧回溯目标位置（pos - vel * latency）。"""
    return (target_pos[0] - target_vel[0] * latency,
            target_pos[1] - target_vel[1] * latency)


def penetration_loss(thickness, angle_cos, base):
    """穿透衰减：按材质厚度与入射角衰减，掠射角衰减更大。"""
    c = max(abs(angle_cos), 1e-6)
    return thickness * base / c


def substep_count(speed, dt, radius):
    """固定子步：每步位移不超过子弹直径，防止低帧率穿墙。"""
    max_step = 2.0 * radius
    if max_step <= 0:
        return 1
    return max(1, math.ceil(speed * dt / max_step))


def gravity_drop(t, gravity):
    """重力下坠：0.5 * g * t^2，客户端预测与服务端校正共用。"""
    return 0.5 * gravity * t * t


def layer_order(shield_layer, body_layer):
    """碰撞层排序：按层号升序结算，护盾与实体顺序确定。"""
    return tuple(sorted((shield_layer, body_layer)))


def spread_order(pellets):
    """霰弹稳定顺序：排序后逐发结算，后坐力叠加顺序确定。"""
    return sorted(pellets)


def rollback_state(health, destroyed):
    """可破坏物回滚：延迟补偿同时回滚血量与销毁状态。"""
    return (health, destroyed)


def platform_local_velocity(world_vel, platform_vel):
    """平台局部速度：弹道在移动平台局部坐标系积分。"""
    return (world_vel[0] - platform_vel[0],
            world_vel[1] - platform_vel[1])


def path_hash(points):
    """穿透路径哈希：记录完整路径供回放，而非只记命中点。"""
    return "|".join(f"{p[0]},{p[1]}" for p in points)


def bullet_id(shooter, shot_index):
    """子弹唯一 id：网络重发时按 id 幂等去重。"""
    return f"{shooter}:{shot_index}"


def hit_time(distance, speed):
    """命中时间。"""
    return distance / speed


def pierce_budget(thickness, budget):
    """穿透预算：按穿透厚度扣减预算。"""
    return budget - thickness


def angle_cos(dx, dy):
    """入射角余弦。"""
    n = math.hypot(dx, dy)
    if n == 0:
        return 0.0
    return dx / n


def trajectory_step(position, velocity, dt, gravity):
    """弹道积分：x 匀速，y 用平均速度（含半步重力），两端一致。"""
    x = position[0] + velocity[0] * dt
    y = position[1] + velocity[1] * dt - 0.5 * gravity * dt * dt
    return (x, y)


def duplicate_guard(seen, bullet_id):
    """重复结算保护：id 未见过才允许结算。"""
    return bullet_id not in seen
