# utils.py
def scroll_to_city(page, city: str):
    result = page.evaluate('''(city) => {
        const labels = [...document.querySelectorAll('label')];
        const element = labels.find(label => label.textContent.trim().toLowerCase() === city.toLowerCase());
        if (element) {
            element.scrollIntoView({ behavior: 'smooth', block: 'center' });
            return 'Element found and scrolled into view';
        } else {
            return 'Element not found';
        }
    }''', city)

def scroll_to_bottom(page):
    page.evaluate("""
            window.scrollTo({
                top: document.body.scrollHeight,
                behavior: 'smooth'
            });
        """)
    page.wait_for_load_state('networkidle')
