BASE_PATH = "notes/"


def getPath(ctx):
    return BASE_PATH + str(ctx.guild.id) + ".txt"
