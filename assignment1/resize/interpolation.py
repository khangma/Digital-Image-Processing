class interpolation:

    def linear_interpolation(self, pt1, pt2, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""

        # Write your code for linear interpolation here
        pt = pt1[1]*(pt2[0]-unknown)/(pt2[0]-pt1[0]) + pt2[1]*(unknown-pt1[0])/(pt2[0]-pt1[0])

        return pt

    def bilinear_interpolation(self, pt1, pt2, pt3, pt4, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        pt1: known point pt3 and f(pt3) or intensity value
        pt2: known point pt4 and f(pt4) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""

        # Write your code for bi-linear interpolation here
        # May be you can reuse or call linear interpolation method to compute this task
        interpoint1 = self.linear_interpolation([pt1[0], pt1[2]], [pt2[0], pt2[2]], unknown[0])
        interpoint2 = self.linear_interpolation([pt3[0], pt3[2]], [pt4[0], pt4[2]], unknown[0])
        result = self.linear_interpolation([pt1[1], interpoint1], [pt3[1], interpoint2], unknown[1])

        return result

