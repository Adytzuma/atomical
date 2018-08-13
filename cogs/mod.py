import discord
import random
from discord.ext import commands
import logging
import traceback
import asyncio
import os
from discord import opus
from asyncio import sleep


class Moderation():
	def __init__(self, bot):
		self.bot = bot
		colors = [discord.Colour.purple(), discord.Colour.blue(), discord.Colour.red(), discord.Colour.green(), discord.Colour.orange()]






	@commands.cooldown(1, 5, commands.BucketType.user)
	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, member: discord.Member = None, *, reason = None):
		'''Ban a member in a guild
		-------------------
		Ex:
		a?ban @Adytzu Bad boy'''
		if member is None:
			await ctx.send("<:AtomicalQuestion:474576686873051136> | Please provide a user to ban")
		if member == ctx.author:
			return await ctx.send("<:AtomicalForbidden:474576377954172949> | You can't ban yourself!")
		if member == self.bot.user:
			return await ctx.send("<:AtomicalForbidden:474576377954172949> | I can't ban myself!")
		if member == ctx.author.guild.owner:
			return await ctx.send("<:AtomicalForbidden:474576377954172949> | I can't ban the owner")
		if member != ctx.author and member != self.bot.user:
			await member.ban()
			await ctx.send(f'<:AtomicalSucces:474568904170274826> | **{member}** just got banned.')





	@commands.cooldown(1, 5, commands.BucketType.user)
	@commands.command()
	@commands.has_permissions(kick_members=True)
	async def kick(self, ctx, member: discord.Member = None, *, reason = None):
		'''Kick a member in a guild
		-------------------
		Ex:
		a?kick @Adytzu Shitposting'''
		if member is None:
			await ctx.send("<:AtomicalQuestion:474576686873051136> | Please provide a user to kick")
		if member == ctx.author:
			return await ctx.send("<:AtomicalForbidden:474576377954172949> | You can't kick yourself!")
		if member == self.bot.user:
			return await ctx.send("<:AtomicalForbidden:474576377954172949> | I can't kick myself!")
		if member == ctx.author.guild.owner:
			return await ctx.send("<:AtomicalForbidden:474576377954172949> | I can't kick the owner")
		if member != ctx.author and member != self.bot.user:
			await member.kick()
			await ctx.send(f'<:AtomicalSucces:474568904170274826> | **{member}** just got kicked.')

	@commands.cooldown(1, 5, commands.BucketType.user)
	@commands.command(aliases= ["clear", "prune"])
	@commands.has_permissions(manage_guild=True)
	async def purge(self, ctx, number : int):
		'''Delete a number of messages in a channel
		-------------------
		Ex:
		a?purge 50'''
		if number>500 or number<0:
			return await ctx.send("<:AtomicalQuestion:474576686873051136> | Invalid amount, maximum is 500.")
		await ctx.message.delete()
		await ctx.channel.purge(limit=number, bulk=True)
		await ctx.message.channel.send(f'<:AtomicalSucces:474568904170274826> | Succefully deleted {int(number)} messages!', delete_after=5)














































def setup(bot):
        bot.add_cog(Moderation(bot))
