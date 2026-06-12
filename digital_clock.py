"""
Digital Clock - Multi Timezone Display
Author: Data Analyst Intern
Description: Real-time digital clock displaying current time in multiple time zones
with GUI support using tkinter
"""

import tkinter as tk
from tkinter import font
from datetime import datetime
import pytz
from typing import List, Tuple

class DigitalClock:
    """
    A digital clock application that displays time in multiple time zones.
    """
    
    def __init__(self, root: tk.Tk, timezones: List[Tuple[str, str]] = None):
        """
        Initialize the digital clock.
        
        Args:
            root: Tkinter root window
            timezones: List of tuples (timezone_name, timezone_code)
                      e.g., [("New York", "America/New_York"), ("London", "Europe/London")]
        """
        self.root = root
        self.root.title("🕐 Digital Clock - Multi Timezone")
        self.root.geometry("1000x500")
        self.root.configure(bg="#1a1a2e")
        self.root.resizable(True, True)
        
        # Default timezones if none provided
        if timezones is None:
            self.timezones = [
                ("🌍 UTC", "UTC"),
                ("🗽 New York (EST)", "America/New_York"),
                ("🇬🇧 London (GMT)", "Europe/London"),
                ("🇮🇳 India (IST)", "Asia/Kolkata"),
                ("🇯🇵 Tokyo (JST)", "Asia/Tokyo"),
                ("🇦🇺 Sydney (AEDT)", "Australia/Sydney"),
                ("🇧🇷 São Paulo (BRT)", "America/Sao_Paulo"),
                ("🇩🇺 Dubai (GST)", "Asia/Dubai"),
        ]
        else:
            self.timezones = timezones
        
        # Font configuration
        self.title_font = font.Font(family="Helvetica", size=24, weight="bold")
        self.time_font = font.Font(family="Courier", size=32, weight="bold")
        self.timezone_font = font.Font(family="Helvetica", size=12, weight="bold")
        self.label_font = font.Font(family="Helvetica", size=10)
        
        # Color scheme
        self.colors = {
            "bg": "#1a1a2e",
            "fg": "#00d4ff",
            "accent": "#ff006e",
            "clock_bg": "#0f3460",
            "text": "#ffffff"
        }
        
        # Create UI
        self.create_widgets()
        
        # Start clock update
        self.update_time()
    
    def create_widgets(self):
        """Create and layout all UI components."""
        
        # Main container
        main_frame = tk.Frame(self.root, bg=self.colors["bg"])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(
            main_frame,
            text="⏰ Digital Clock - Multi Timezone Display",
            font=self.title_font,
            bg=self.colors["bg"],
            fg=self.colors["accent"]
        )
        title_label.pack(pady=(0, 20))
        
        # Subtitle
        subtitle_label = tk.Label(
            main_frame,
            text="Real-time clock showing current time across different time zones",
            font=self.label_font,
            bg=self.colors["bg"],
            fg=self.colors["fg"]
        )
        subtitle_label.pack(pady=(0, 20))
        
        # Clocks grid container
        self.clocks_frame = tk.Frame(main_frame, bg=self.colors["bg"])
        self.clocks_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create clock widgets for each timezone
        self.clock_labels = {}
        for idx, (tz_name, tz_code) in enumerate(self.timezones):
            # Calculate grid position (2 columns)
            row = idx // 2
            col = idx % 2
            
            # Container for each clock
            clock_container = tk.Frame(
                self.clocks_frame,
                bg=self.colors["clock_bg"],
                relief=tk.RIDGE,
                bd=2,
                highlightthickness=2,
                highlightbackground=self.colors["accent"]
            )
            clock_container.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            
            # Timezone name
            tz_label = tk.Label(
                clock_container,
                text=tz_name,
                font=self.timezone_font,
                bg=self.colors["clock_bg"],
                fg=self.colors["accent"],
                pady=5
            )
            tz_label.pack()
            
            # Time display
            time_label = tk.Label(
                clock_container,
                text="00:00:00",
                font=self.time_font,
                bg=self.colors["clock_bg"],
                fg=self.colors["fg"],
                family="Courier",
                pady=10
            )
            time_label.pack()
            
            # Date display
            date_label = tk.Label(
                clock_container,
                text="YYYY-MM-DD",
                font=self.label_font,
                bg=self.colors["clock_bg"],
                fg=self.colors["text"],
                pady=5
            )
            date_label.pack(pady=(0, 10))
            
            # Store references
            self.clock_labels[tz_code] = {
                'time': time_label,
                'date': date_label,
                'tz_name': tz_name
            }
        
        # Configure grid weights for responsiveness
        for i in range(len(self.timezones)):
            if i // 2 >= 0:
                self.clocks_frame.grid_rowconfigure(i // 2, weight=1)
        self.clocks_frame.grid_columnconfigure(0, weight=1)
        self.clocks_frame.grid_columnconfigure(1, weight=1)
        
        # Footer with update info
        footer_frame = tk.Frame(main_frame, bg=self.colors["bg"])
        footer_frame.pack(fill=tk.X, pady=(20, 0))
        
        self.update_label = tk.Label(
            footer_frame,
            text="Updating in real-time...",
            font=self.label_font,
            bg=self.colors["bg"],
            fg=self.colors["fg"]
        )
        self.update_label.pack(side=tk.LEFT)
    
    def update_time(self):
        """Update the time display for all timezones."""
        try:
            current_utc = datetime.now(pytz.UTC)
            
            for tz_code, labels in self.clock_labels.items():
                # Get timezone and convert time
                tz = pytz.timezone(tz_code)
                local_time = current_utc.astimezone(tz)
                
                # Format time and date
                time_str = local_time.strftime("%H:%M:%S")
                date_str = local_time.strftime("%Y-%m-%d")
                day_str = local_time.strftime("%A")
                
                # Update labels
                labels['time'].config(text=time_str)
                labels['date'].config(text=f"{date_str} ({day_str})")
            
            # Update last update time
            self.update_label.config(
                text=f"Last updated: {datetime.now().strftime('%H:%M:%S')}"
            )
        
        except Exception as e:
            print(f"Error updating time: {e}")
        
        # Schedule next update (every 1000ms = 1 second)
        self.root.after(1000, self.update_time)

def main():
    """Main function to run the digital clock application."""
    root = tk.Tk()
    
    # Initialize clock with default timezones
    clock = DigitalClock(root)
    
    # Center window on screen
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")
    
    # Run the application
    root.mainloop()

if __name__ == "__main__":
    main()
