import { validateDate } from '../../src/validators/date';

describe('validateDate', () => {
    it('should return true for valid date formats', () => {
        expect(validateDate('2023-10-01')).toBe(true);
        expect(validateDate('01/10/2023')).toBe(true);
        expect(validateDate('10-01-2023')).toBe(true);
    });

    it('should return false for invalid date formats', () => {
        expect(validateDate('2023-13-01')).toBe(false);
        expect(validateDate('2023-02-30')).toBe(false);
        expect(validateDate('01/2023/10')).toBe(false);
        expect(validateDate('not-a-date')).toBe(false);
    });

    it('should return false for empty strings', () => {
        expect(validateDate('')).toBe(false);
    });
});