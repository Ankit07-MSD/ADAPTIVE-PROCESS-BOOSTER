#!/usr/bin/env python3
"""
Advanced Architecture Diagram Generator using 'diagrams' library
Alternative method for creating architecture diagrams
Install: pip install diagrams
"""

try:
    from diagrams import Diagram, Cluster, Edge
    from diagrams.onprem.client import User
    from diagrams.programming.language import Python
    from diagrams.onprem.compute import Server
    from diagrams.onprem.monitoring import Prometheus
    from diagrams.generic.storage import Storage
    from diagrams.onprem.network import Internet
    DIAGRAMS_AVAILABLE = True
except ImportError:
    DIAGRAMS_AVAILABLE = False
    print("Note: 'diagrams' library not installed.")
    print("Install with: pip install diagrams")
    print("This is an alternative method. Using matplotlib method instead.\n")


def create_diagrams_architecture():
    """Create architecture diagram using diagrams library."""
    if not DIAGRAMS_AVAILABLE:
        print("⚠️  diagrams library not available. Skipping this method.")
        return None
    
    with Diagram("Adaptive Process Booster - System Architecture", 
                 filename="architecture_diagrams_lib", 
                 show=False, direction="TB"):
        
        with Cluster("GUI Layer"):
            gui = Python("Tkinter GUI")
            monitor = Server("Process Monitor")
            resources = Server("System Resources")
            history = Storage("History & Logs")
            
            gui >> monitor
            gui >> resources
            gui >> history
        
        with Cluster("Background Thread"):
            thread = Python("Monitoring Thread")
            scanner = Server("Process Scanner")
            calculator = Server("Score Calculator")
            booster = Server("Auto-Booster")
            
            thread >> scanner
            thread >> calculator
            thread >> booster
        
        with Cluster("Operating System"):
            os = Server("OS Kernel")
            process_mgr = Server("Process Manager")
            priority = Server("Priority Control")
            
            os >> process_mgr
            os >> priority
        
        gui >> Edge(label="root.after()\nThread-Safe") >> thread
        thread >> Edge(label="psutil") >> os
    
    print("✅ Architecture diagram created: architecture_diagrams_lib.png")
    return "architecture_diagrams_lib.png"


def create_flowchart_diagram():
    """Create flowchart using matplotlib."""
    try:
        import matplotlib.pyplot as plt
        import matplotlib.patches as mpatches
        from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
        
        fig, ax = plt.subplots(1, 1, figsize=(14, 10))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 12)
        ax.axis('off')
        
        # Title
        ax.text(5, 11.5, 'Process Monitoring Flowchart', 
                ha='center', va='center', fontsize=18, fontweight='bold',
                color='#2C3E50')
        
        # Flowchart boxes
        steps = [
            (5, 10, 'Start Application', '#2E86AB'),
            (5, 8.5, 'Initialize GUI', '#06A77D'),
            (5, 7, 'Start Background Thread', '#F18F01'),
            (2, 5.5, 'Scan Processes\n(psutil)', '#9B59B6'),
            (5, 5.5, 'Calculate Scores', '#E74C3C'),
            (8, 5.5, 'Check Auto-Boost', '#3498DB'),
            (5, 4, 'Update GUI\n(root.after())', '#16A085'),
            (5, 2.5, 'Wait 1 Second', '#95A5A6'),
            (5, 1, 'Repeat Loop', '#34495E')
        ]
        
        for x, y, text, color in steps:
            box = FancyBboxPatch((x-1, y-0.4), 2, 0.8, 
                                boxstyle="round,pad=0.1", 
                                edgecolor='black', facecolor=color, 
                                linewidth=2, zorder=1)
            ax.add_patch(box)
            ax.text(x, y, text, 
                   ha='center', va='center', fontsize=10, fontweight='bold',
                   color='white')
        
        # Arrows
        arrow_coords = [
            ((5, 9.6), (5, 8.9)),
            ((5, 8.1), (5, 7.4)),
            ((5, 6.6), (3, 5.9)),
            ((2.5, 5.5), (4.5, 5.5)),
            ((5.5, 5.5), (7.5, 5.5)),
            ((8, 5.1), (5, 4.4)),
            ((5, 3.6), (5, 2.9)),
            ((5, 2.1), (5, 1.4)),
            ((5, 0.6), (5, 7.4))  # Loop back
        ]
        
        for (x1, y1), (x2, y2) in arrow_coords:
            arrow = FancyArrowPatch((x1, y1), (x2, y2), 
                                   arrowstyle='->', mutation_scale=20,
                                   color='#34495E', linewidth=2, zorder=2)
            ax.add_patch(arrow)
        
        # Loop indicator
        ax.text(6, 4.5, 'Loop Back', 
               ha='left', va='center', fontsize=9, style='italic',
               bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', 
                        edgecolor='orange', linewidth=1.5))
        
        filename = 'Process_Flowchart_Diagram.png'
        plt.tight_layout()
        plt.savefig(filename, format='png', dpi=300, bbox_inches='tight')
        print(f"✅ Flowchart diagram saved as: {filename}")
        return filename
        
    except ImportError:
        print("⚠️  matplotlib not available")
        return None


if __name__ == "__main__":
    print("=" * 60)
    print("Advanced Architecture Diagram Generator")
    print("=" * 60)
    print()
    
    # Try diagrams library method
    if DIAGRAMS_AVAILABLE:
        print("Using 'diagrams' library method...")
        create_diagrams_architecture()
        print()
    
    # Create flowchart
    print("Creating flowchart diagram...")
    create_flowchart_diagram()
    print()
    
    print("✅ Advanced diagrams created!")




