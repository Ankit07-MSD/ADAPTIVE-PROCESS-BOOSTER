#!/usr/bin/env python3
"""
Create System Architecture Diagram for Adaptive Process Booster
Supports multiple output formats: PNG, SVG, PDF
"""

try:
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
    import matplotlib.patches as patches
except ImportError:
    print("Installing matplotlib...")
    import subprocess
    subprocess.check_call(["pip", "install", "matplotlib"])
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
    import matplotlib.patches as patches

def create_architecture_diagram(output_format='png'):
    """
    Create high-quality system architecture diagram.
    
    Args:
        output_format: 'png', 'svg', or 'pdf'
    """
    # Create figure with higher quality settings
    fig, ax = plt.subplots(1, 1, figsize=(16, 12), dpi=100)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 11)
    ax.axis('off')
    
    # Enable anti-aliasing for better quality
    plt.rcParams['figure.dpi'] = 100
    plt.rcParams['savefig.dpi'] = 600  # High resolution
    plt.rcParams['savefig.facecolor'] = 'white'
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans', 'Liberation Sans']
    plt.rcParams['font.weight'] = 'bold'
    plt.rcParams['axes.edgecolor'] = 'none'
    
    # Enhanced color palette with gradients
    gui_color = '#1E6A8E'  # Deeper blue
    gui_color_light = '#2E86AB'  # Lighter blue for components
    thread_color = '#048A5F'  # Deeper green
    thread_color_light = '#06A77D'  # Lighter green
    os_color = '#D97706'  # Deeper orange
    os_color_light = '#F18F01'  # Lighter orange
    text_color = '#FFFFFF'
    arrow_color = '#495057'  # Darker gray for better visibility
    shadow_color = '#000000'
    
    # Title with shadow effect
    title_text = 'Adaptive Process Booster - System Architecture'
    ax.text(5.05, 10.45, title_text, 
            ha='center', va='center', fontsize=22, fontweight='bold',
            color='#1a1a1a', alpha=0.3, zorder=0)  # Shadow
    ax.text(5, 10.5, title_text, 
            ha='center', va='center', fontsize=22, fontweight='bold',
            color='#2C3E50', zorder=1)
    
    # GUI Layer - Centered and properly sized with shadow
    gui_box_width = 7.5
    gui_box_height = 2.2
    gui_box_x = (10 - gui_box_width) / 2  # Center horizontally
    gui_box_y = 7.5
    
    # Shadow for GUI box
    gui_box_shadow = FancyBboxPatch((gui_box_x + 0.08, gui_box_y - 0.08), 
                                    gui_box_width, gui_box_height, 
                                    boxstyle="round,pad=0.1", 
                                    edgecolor='none', facecolor='#000000', 
                                    alpha=0.15, linewidth=0, zorder=0)
    ax.add_patch(gui_box_shadow)
    
    gui_box = FancyBboxPatch((gui_box_x, gui_box_y), gui_box_width, gui_box_height, 
                             boxstyle="round,pad=0.1", 
                             edgecolor='#0F4C75', facecolor=gui_color, 
                             linewidth=3.5, zorder=1)
    ax.add_patch(gui_box)
    
    # Title text with shadow
    ax.text(5.02, 8.78, 'GUI Layer (Tkinter)', 
            ha='center', va='center', fontsize=17, fontweight='bold',
            color='#000000', alpha=0.2, zorder=2)  # Shadow
    ax.text(5, 8.8, 'GUI Layer (Tkinter)', 
            ha='center', va='center', fontsize=17, fontweight='bold',
            color=text_color, zorder=3)
    
    # GUI Components - Evenly spaced
    tab_width = 2.1
    tab_height = 0.7
    tab_spacing = 0.15
    total_tabs_width = 3 * tab_width + 2 * tab_spacing
    tab_start_x = (10 - total_tabs_width) / 2  # Center tabs
    
    tab1 = FancyBboxPatch((tab_start_x, gui_box_y + 0.3), tab_width, tab_height, 
                          boxstyle="round,pad=0.05", 
                          edgecolor='white', facecolor='#1A5F7A', 
                          linewidth=1.5, zorder=2)
    ax.add_patch(tab1)
    ax.text(tab_start_x + tab_width/2, gui_box_y + 0.65, 'Process Monitor', 
            ha='center', va='center', fontsize=9, color=text_color, fontweight='bold')
    
    tab2_x = tab_start_x + tab_width + tab_spacing
    tab2 = FancyBboxPatch((tab2_x, gui_box_y + 0.3), tab_width, tab_height, 
                          boxstyle="round,pad=0.05", 
                          edgecolor='white', facecolor='#1A5F7A', 
                          linewidth=1.5, zorder=2)
    ax.add_patch(tab2)
    ax.text(tab2_x + tab_width/2, gui_box_y + 0.65, 'System Resources', 
            ha='center', va='center', fontsize=9, color=text_color, fontweight='bold')
    
    tab3_x = tab2_x + tab_width + tab_spacing
    tab3 = FancyBboxPatch((tab3_x, gui_box_y + 0.3), tab_width, tab_height, 
                          boxstyle="round,pad=0.05", 
                          edgecolor='white', facecolor='#1A5F7A', 
                          linewidth=1.5, zorder=2)
    ax.add_patch(tab3)
    ax.text(tab3_x + tab_width/2, gui_box_y + 0.65, 'History & Logs', 
            ha='center', va='center', fontsize=9, color=text_color, fontweight='bold')
    
    # Arrow from GUI to Thread
    arrow1 = FancyArrowPatch((5, gui_box_y), (5, 6.2), 
                             arrowstyle='->', mutation_scale=25,
                             color=arrow_color, linewidth=3, zorder=3)
    ax.add_patch(arrow1)
    ax.text(5.6, 6.7, 'Thread-Safe Communication\n(root.after())', 
            ha='left', va='center', fontsize=9, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white', 
                     edgecolor=arrow_color, linewidth=2))
    
    # Background Thread Layer - Centered
    thread_box_width = 7.5
    thread_box_height = 1.8
    thread_box_x = (10 - thread_box_width) / 2
    thread_box_y = 4.2
    
    thread_box = FancyBboxPatch((thread_box_x, thread_box_y), thread_box_width, thread_box_height, 
                                boxstyle="round,pad=0.1", 
                                edgecolor='black', facecolor=thread_color, 
                                linewidth=2.5, zorder=1)
    ax.add_patch(thread_box)
    ax.text(5, 5.4, 'Background Monitoring Thread', 
            ha='center', va='center', fontsize=15, fontweight='bold',
            color=text_color)
    
    # Thread Components - Evenly spaced
    comp_width = 1.65
    comp_height = 0.55
    comp_spacing = 0.1
    total_comp_width = 4 * comp_width + 3 * comp_spacing
    comp_start_x = (10 - total_comp_width) / 2
    
    comp1 = FancyBboxPatch((comp_start_x, thread_box_y + 0.25), comp_width, comp_height, 
                          boxstyle="round,pad=0.05", 
                          edgecolor='white', facecolor='#048A5F', 
                          linewidth=1.5, zorder=2)
    ax.add_patch(comp1)
    ax.text(comp_start_x + comp_width/2, thread_box_y + 0.525, 'Process\nScanning', 
            ha='center', va='center', fontsize=8, color=text_color, fontweight='bold')
    
    comp2_x = comp_start_x + comp_width + comp_spacing
    comp2 = FancyBboxPatch((comp2_x, thread_box_y + 0.25), comp_width, comp_height, 
                          boxstyle="round,pad=0.05", 
                          edgecolor='white', facecolor='#048A5F', 
                          linewidth=1.5, zorder=2)
    ax.add_patch(comp2)
    ax.text(comp2_x + comp_width/2, thread_box_y + 0.525, 'System\nStats', 
            ha='center', va='center', fontsize=8, color=text_color, fontweight='bold')
    
    comp3_x = comp2_x + comp_width + comp_spacing
    comp3 = FancyBboxPatch((comp3_x, thread_box_y + 0.25), comp_width, comp_height, 
                          boxstyle="round,pad=0.05", 
                          edgecolor='white', facecolor='#048A5F', 
                          linewidth=1.5, zorder=2)
    ax.add_patch(comp3)
    ax.text(comp3_x + comp_width/2, thread_box_y + 0.525, 'Score\nCalculation', 
            ha='center', va='center', fontsize=8, color=text_color, fontweight='bold')
    
    comp4_x = comp3_x + comp_width + comp_spacing
    comp4 = FancyBboxPatch((comp4_x, thread_box_y + 0.25), comp_width, comp_height, 
                          boxstyle="round,pad=0.05", 
                          edgecolor='white', facecolor='#048A5F', 
                          linewidth=1.5, zorder=2)
    ax.add_patch(comp4)
    ax.text(comp4_x + comp_width/2, thread_box_y + 0.525, 'Auto-Boost\nLogic', 
            ha='center', va='center', fontsize=8, color=text_color, fontweight='bold')
    
    # Arrow from Thread to OS
    arrow2 = FancyArrowPatch((5, thread_box_y), (5, 2.8), 
                             arrowstyle='->', mutation_scale=25,
                             color=arrow_color, linewidth=3, zorder=3)
    ax.add_patch(arrow2)
    ax.text(5.6, 3.5, 'System Calls\n(psutil)', 
            ha='left', va='center', fontsize=9, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white', 
                     edgecolor=arrow_color, linewidth=2))
    
    # OS Layer - Centered
    os_box_width = 7.5
    os_box_height = 1.3
    os_box_x = (10 - os_box_width) / 2
    os_box_y = 1.3
    
    os_box = FancyBboxPatch((os_box_x, os_box_y), os_box_width, os_box_height, 
                            boxstyle="round,pad=0.1", 
                            edgecolor='black', facecolor=os_color, 
                            linewidth=2.5, zorder=1)
    ax.add_patch(os_box)
    ax.text(5, 2.15, 'Operating System', 
            ha='center', va='center', fontsize=15, fontweight='bold',
            color=text_color)
    
    # OS Components - Evenly spaced
    os_comp_width = 2.2
    os_comp_height = 0.5
    os_comp_spacing = 0.1
    total_os_comp_width = 3 * os_comp_width + 2 * os_comp_spacing
    os_comp_start_x = (10 - total_os_comp_width) / 2
    
    os_comp1 = FancyBboxPatch((os_comp_start_x, os_box_y + 0.2), os_comp_width, os_comp_height, 
                             boxstyle="round,pad=0.05", 
                             edgecolor='white', facecolor='#C96F00', 
                             linewidth=1.5, zorder=2)
    ax.add_patch(os_comp1)
    ax.text(os_comp_start_x + os_comp_width/2, os_box_y + 0.45, 'Process\nManagement', 
            ha='center', va='center', fontsize=8, color=text_color, fontweight='bold')
    
    os_comp2_x = os_comp_start_x + os_comp_width + os_comp_spacing
    os_comp2 = FancyBboxPatch((os_comp2_x, os_box_y + 0.2), os_comp_width, os_comp_height, 
                             boxstyle="round,pad=0.05", 
                             edgecolor='white', facecolor='#C96F00', 
                             linewidth=1.5, zorder=2)
    ax.add_patch(os_comp2)
    ax.text(os_comp2_x + os_comp_width/2, os_box_y + 0.45, 'Priority\nControl', 
            ha='center', va='center', fontsize=8, color=text_color, fontweight='bold')
    
    os_comp3_x = os_comp2_x + os_comp_width + os_comp_spacing
    os_comp3 = FancyBboxPatch((os_comp3_x, os_box_y + 0.2), os_comp_width, os_comp_height, 
                             boxstyle="round,pad=0.05", 
                             edgecolor='white', facecolor='#C96F00', 
                             linewidth=1.5, zorder=2)
    ax.add_patch(os_comp3)
    ax.text(os_comp3_x + os_comp_width/2, os_box_y + 0.45, 'Resource\nAllocation', 
            ha='center', va='center', fontsize=8, color=text_color, fontweight='bold')
    
    # Save figure
    filename = f'System_Architecture_Diagram.{output_format}'
    plt.tight_layout()
    plt.savefig(filename, format=output_format, dpi=300, bbox_inches='tight', pad_inches=0.2)
    print(f"✅ Architecture diagram saved as: {filename}")
    print(f"📊 Format: {output_format.upper()}")
    return filename


def create_threading_diagram(output_format='png'):
    """Create threading model diagram."""
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Colors
    main_color = '#2E86AB'
    bg_color = '#06A77D'
    arrow_color = '#6C757D'
    text_color = '#FFFFFF'
    
    # Title
    ax.text(5, 9.5, 'Multi-Threading Architecture', 
            ha='center', va='center', fontsize=18, fontweight='bold',
            color='#2C3E50')
    
    # Main Thread (Left)
    main_box = FancyBboxPatch((0.5, 1), 4, 7, 
                              boxstyle="round,pad=0.1", 
                              edgecolor='black', facecolor=main_color, 
                              linewidth=2, zorder=1)
    ax.add_patch(main_box)
    ax.text(2.5, 7.5, 'Main Thread (GUI)', 
            ha='center', va='center', fontsize=14, fontweight='bold',
            color=text_color)
    
    # Main Thread Components
    main_components = [
        'User Interactions',
        'GUI Updates',
        'Event Handling',
        'Window Management'
    ]
    
    y_pos = 6
    for comp in main_components:
        comp_box = FancyBboxPatch((0.8, y_pos - 0.3), 3.4, 0.5, 
                                  boxstyle="round,pad=0.05", 
                                  edgecolor='white', facecolor='#1A5F7A', 
                                  linewidth=1.5, zorder=2)
        ax.add_patch(comp_box)
        ax.text(2.5, y_pos, comp, 
                ha='center', va='center', fontsize=10, color=text_color)
        y_pos -= 1
    
    # Background Thread (Right)
    bg_box = FancyBboxPatch((5.5, 1), 4, 7, 
                           boxstyle="round,pad=0.1", 
                           edgecolor='black', facecolor=bg_color, 
                           linewidth=2, zorder=1)
    ax.add_patch(bg_box)
    ax.text(7.5, 7.5, 'Background Thread', 
            ha='center', va='center', fontsize=14, fontweight='bold',
            color=text_color)
    
    # Background Thread Components
    bg_components = [
        'Process Scanning',
        'System Stats',
        'Score Calculation',
        'Auto-Boost Logic'
    ]
    
    y_pos = 6
    for comp in bg_components:
        comp_box = FancyBboxPatch((5.8, y_pos - 0.3), 3.4, 0.5, 
                                  boxstyle="round,pad=0.05", 
                                  edgecolor='white', facecolor='#048A5F', 
                                  linewidth=1.5, zorder=2)
        ax.add_patch(comp_box)
        ax.text(7.5, y_pos, comp, 
                ha='center', va='center', fontsize=10, color=text_color)
        y_pos -= 1
    
    # Arrows
    arrow = FancyArrowPatch((4.5, 4.5), (5.5, 4.5), 
                           arrowstyle='<->', mutation_scale=25,
                           color=arrow_color, linewidth=3, zorder=3)
    ax.add_patch(arrow)
    ax.text(5, 5, 'root.after()\nThread-Safe\nCommunication', 
            ha='center', va='center', fontsize=10, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white', 
                     edgecolor=arrow_color, linewidth=2))
    
    # Benefits box
    benefits_box = FancyBboxPatch((0.5, 0.2), 9, 0.6, 
                                 boxstyle="round,pad=0.1", 
                                 edgecolor='black', facecolor='#F8F9FA', 
                                 linewidth=2, zorder=1)
    ax.add_patch(benefits_box)
    ax.text(5, 0.5, 'Benefits: Non-Blocking • Real-Time • Efficient • Smooth UX', 
            ha='center', va='center', fontsize=11, 
            color='#2C3E50', fontweight='bold')
    
    filename = f'Threading_Architecture_Diagram.{output_format}'
    plt.tight_layout()
    plt.savefig(filename, format=output_format, dpi=300, bbox_inches='tight')
    print(f"✅ Threading diagram saved as: {filename}")
    return filename


def create_data_flow_diagram(output_format='png'):
    """Create data flow diagram."""
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(6, 9.5, 'Data Flow in Adaptive Process Booster', 
            ha='center', va='center', fontsize=18, fontweight='bold',
            color='#2C3E50')
    
    # Process flow boxes
    boxes = [
        (1, 7, 'Process\nScanning', '#2E86AB'),
        (4, 7, 'Data\nCollection', '#06A77D'),
        (7, 7, 'Score\nCalculation', '#F18F01'),
        (10, 7, 'Auto-Boost\nDecision', '#9B59B6'),
        (4, 4, 'GUI\nUpdate', '#E74C3C'),
        (7, 4, 'User\nInteraction', '#3498DB'),
        (10, 4, 'Priority\nChange', '#16A085')
    ]
    
    for x, y, text, color in boxes:
        box = FancyBboxPatch((x-0.8, y-0.5), 1.6, 1, 
                            boxstyle="round,pad=0.1", 
                            edgecolor='black', facecolor=color, 
                            linewidth=2, zorder=1)
        ax.add_patch(box)
        ax.text(x, y, text, 
                ha='center', va='center', fontsize=11, fontweight='bold',
                color='white')
    
    # Arrows
    arrows = [
        ((1.8, 7), (3.2, 7), 'psutil'),
        ((4.8, 7), (6.2, 7), 'Calculate'),
        ((7.8, 7), (9.2, 7), 'Check'),
        ((4, 6.5), (4, 4.5), 'Update'),
        ((7, 6.5), (7, 4.5), 'Display'),
        ((10, 6.5), (10, 4.5), 'Apply'),
        ((10.8, 4), (11.5, 4), 'OS')
    ]
    
    for (x1, y1), (x2, y2), label in arrows:
        arrow = FancyArrowPatch((x1, y1), (x2, y2), 
                               arrowstyle='->', mutation_scale=20,
                               color='#34495E', linewidth=2, zorder=2)
        ax.add_patch(arrow)
        if label:
            mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
            ax.text(mid_x, mid_y, label, 
                   ha='center', va='center', fontsize=9,
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 
                            edgecolor='#34495E', linewidth=1))
    
    filename = f'Data_Flow_Diagram.{output_format}'
    plt.tight_layout()
    plt.savefig(filename, format=output_format, dpi=300, bbox_inches='tight')
    print(f"✅ Data flow diagram saved as: {filename}")
    return filename


def convert_to_multiple_formats():
    """Create diagrams in multiple formats."""
    formats = ['png', 'svg', 'pdf']
    
    print("Creating architecture diagrams in multiple formats...\n")
    
    for fmt in formats:
        try:
            print(f"📊 Creating {fmt.upper()} format...")
            create_architecture_diagram(fmt)
            create_threading_diagram(fmt)
            create_data_flow_diagram(fmt)
            print()
        except Exception as e:
            print(f"⚠️  Error creating {fmt} format: {e}\n")
    
    print("✅ All diagrams created successfully!")


if __name__ == "__main__":
    print("=" * 60)
    print("Adaptive Process Booster - Architecture Diagram Generator")
    print("=" * 60)
    print()
    
    # Create diagrams in PNG format (default)
    print("Creating architecture diagrams...\n")
    
    try:
        create_architecture_diagram('png')
        create_threading_diagram('png')
        create_data_flow_diagram('png')
        
        print("\n" + "=" * 60)
        print("✅ All diagrams created successfully!")
        print("=" * 60)
        print("\n💡 To create in multiple formats (PNG, SVG, PDF), run:")
        print("   convert_to_multiple_formats()")
        print("\n📁 Files created:")
        print("   - System_Architecture_Diagram.png")
        print("   - Threading_Architecture_Diagram.png")
        print("   - Data_Flow_Diagram.png")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nTroubleshooting:")
        print("1. Make sure matplotlib is installed: pip install matplotlib")
        print("2. Check if you have write permissions")
        print("3. Ensure no other program is using the output files")

