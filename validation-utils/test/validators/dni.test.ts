import { validateDNI } from '../../src/validators/dni';

describe('validateDNI', () => {
    it('should return true for a valid DNI', () => {
        expect(validateDNI('12345678A')).toBe(true);
    });

    it('should return false for an invalid DNI with incorrect format', () => {
        expect(validateDNI('1234567A')).toBe(false);
    });

    it('should return false for a DNI with invalid letter', () => {
        expect(validateDNI('12345678B')).toBe(false);
    });

    it('should return false for a DNI that is too short', () => {
        expect(validateDNI('1234567')).toBe(false);
    });

    it('should return false for a DNI that is too long', () => {
        expect(validateDNI('123456789A')).toBe(false);
    });

    it('should return false for a DNI with non-numeric characters', () => {
        expect(validateDNI('12345678Z')).toBe(false);
    });
});