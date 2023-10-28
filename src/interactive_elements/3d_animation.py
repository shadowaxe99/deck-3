```python
import bpy

def create_ai_agent(agent_name, location):
    bpy.ops.mesh.primitive_uv_sphere_add(location=location)
    bpy.context.active_object.name = agent_name

def animate_ai_agents():
    scene = bpy.context.scene
    for frame in range(0, 250):
        scene.frame_set(frame)
        for obj in scene.objects:
            if "AI_Agent" in obj.name:
                obj.location[0] += 0.1
                obj.keyframe_insert(data_path="location", index=0)

def create_3d_animation():
    for i in range(50):
        agent_name = f"AI_Agent_{i}"
        location = (i*0.5, i*0.5, i*0.5)
        create_ai_agent(agent_name, location)
    animate_ai_agents()

if __name__ == "__main__":
    create_3d_animation()
```