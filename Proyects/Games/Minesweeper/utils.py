import settings as st 

def height_prct(percentage):
    return (st.HEIGHT / 100) * percentage


def width_prct(percentage):
    return (st.WIDTH / 100) * percentage

if __name__ == "__main__":
    print(height_prct(100))
    print(width_prct(100))