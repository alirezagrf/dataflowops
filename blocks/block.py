import os
from prefect.blocks.system import Secret,String

String(value=os.getenv("MY_SECRET")).save("my-secret",overwrite=True)

