import asyncio

async def print_with_delay(items):
    delay = 1
    last_index = len(items)
    for index, item in enumerate(items):
        # very important to not sleep after the last iteration
        if index != last_index:
            await asyncio.sleep(delay)
        delay *= 2
        print(item)

async def print_array():
    items = ["a", "b", "c", "d"]
    await print_with_delay(items)

asyncio.run(print_array())
