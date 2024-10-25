extends RigidBody2D


# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass
	
func _physics_process(delta: float) -> void:
	pass
	
func _integrate_forces(state: PhysicsDirectBodyState2D) -> void:
	
	var turning_force = 5000
	var turning_dir = 0
	
	if (Input.is_action_pressed("turn_counterclockwise")):
		turning_dir -= 1
	if (Input.is_action_pressed("turn_clockwise")):
		turning_dir += 1
		
	apply_torque(turning_force * turning_dir)
	
	pass
