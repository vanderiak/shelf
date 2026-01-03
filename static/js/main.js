tailwind.config = {
    darkMode: "class",
    theme: {
        extend: {
            colors: {
                "primary": "#2563eb","secondary": "#3b82f6","background-light": "#f8fafc","background-dark": "#1a202c","panel-light": "#ffffff","panel-dark": "#2d3748","text-primary": "#1e293b","text-secondary": "#475569","border-light": "#e2e8f0","border-dark": "#4a5568",},
                fontFamily: {
                    "sans": ["Inter", "sans-serif"],},
                    borderRadius: {"DEFAULT": "0.5rem", "lg": "0.75rem", "xl": "1rem", "full": "9999px"},
                    boxShadow: {
                        'shelf-inner': 'inset 0 4px 10px -5px rgba(0, 0, 0, 0.2)','book': '1px 0 3px rgba(0,0,0,0.1), inset 1px 0 1px rgba(255,255,255,0.1), inset -1px 0 1px rgba(0,0,0,0.1)',
                        'panel': '0 4px 12px rgba(0,0,0,0.08)',
                    }
                },
            },
        }