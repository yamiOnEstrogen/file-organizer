import talents from "../models/talents";
import { formatDateTime, getAmountOfDays, formatDate } from "./date";
import { Model } from "mongoose";
import TwitterService from "../services/twitter";

export async function getAllTalents() {
  const talentData = await talents.find({});
  const formattedTalents = talentData.map((talent) => ({
    name: talent.name,
    description: talent.description,
    image: talent.image,
    socials: talent.socials,
    //@ts-ignore
    createdAt: formatDate(new Date(talent.createdAt)),
    //@ts-ignore
    createdTime: getAmountOfDays(new Date(talent.createdAt)),
    //@ts-ignore
    renderdTime: formatDateTime(new Date(talent.createdAt)),
    icon_color: talent.icon_color,
  }));

  return formattedTalents;
}

export async function getTalent(name: string) {
  const talentData = await talents
    .find({ name: { $regex: new RegExp(`^${name}$`, "i") } })
    .exec();

  if (!talentData) return null;

  const formattedTalents = talentData.map((talent) => ({
    name: talent.name,
    description: talent.description,
    image: talent.image,
    socials: talent.socials,
    //@ts-ignore
    createdAt: formatDate(new Date(talent.createdAt)),
    //@ts-ignore
    createdTime: getAmountOfDays(new Date(talent.createdAt)),
    //@ts-ignore
    renderdTime: formatDateTime(new Date(talent.createdAt)),
    icon_color: talent.icon_color,
    
  }));

  return formattedTalents[0];
}

export async function getAllTalentNames() {
  const talentData = await talents.find({});
  const talentNames = talentData.map((talent) => talent.name);
  return talentNames;
}
