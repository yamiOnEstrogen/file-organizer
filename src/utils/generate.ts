import crypto from "crypto";
import axios from "axios";

export function generateCardId() {
    return Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15);
}

export function createVerificationCode() {
    // Make it a UUID
    const uuid = crypto.randomBytes(16).toString("hex");
    return uuid;
}

export function getOpenApiKey() {
   return null;
}

export function getStringLength(str: string) {
    return str.length;
}